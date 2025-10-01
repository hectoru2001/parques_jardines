// offline.js - Versión 100% móvil-safe
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form[data-form-name="riego-chamizal"]');
    const btn = document.getElementById('btn-guardar-offline');
    if (!form || !btn) return;

    const API_URL = '/formularios/api/guardar-riego-chamizal/';
    let isSubmitting = false;

    // --- IndexedDB (ligero) ---
    const getDB = () => {
        return new Promise((resolve, reject) => {
            const req = indexedDB.open('RiegoDB', 1);
            req.onsuccess = () => resolve(req.result);
            req.onupgradeneeded = (e) => {
                e.target.result.createObjectStore('pendientes', { autoIncrement: true });
            };
            req.onerror = () => reject(req.error);
        });
    };

    const guardarPendiente = async (data) => {
        const db = await getDB();
        const tx = db.transaction('pendientes', 'readwrite');
        tx.objectStore('pendientes').add({ data, ts: Date.now() });
        await tx.complete;
    };

    const enviar = async (data) => {
        try {
            const res = await fetch(API_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            return res.ok && (await res.json()).status === 'ok';
        } catch {
            return false;
        }
    };

    const notificar = (msg) => {
        let el = document.getElementById('notif-offline');
        if (!el) {
            el = document.createElement('div');
            el.id = 'notif-offline';
            el.style.cssText = `position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:#000;color:#fff;padding:12px 20px;border-radius:8px;z-index:10000;font-size:16px;`;
            document.body.appendChild(el);
        }
        el.textContent = msg;
        el.style.display = 'block';
        setTimeout(() => el.style.display = 'none', 3000);
    };

    // ✅ Solo escuchamos el clic del botón (no submit)
    btn.addEventListener('click', async () => {
        if (isSubmitting) return;
        isSubmitting = true;

        // Desactivar visualmente
        const txt = btn.innerHTML;
        btn.disabled = true;
        btn.innerHTML = 'Guardando...';

        const data = {};
        new FormData(form).forEach((v, k) => data[k] = v);

        if (navigator.onLine) {
            if (await enviar(data)) {
                window.location.href = '/menu/';
            } else {
                await guardarPendiente(data);
                notificar('⚠️ Guardado local. Se enviará después.');
            }
        } else {
            await guardarPendiente(data);
            notificar('📱 Sin conexión. Guardado localmente.');
        }

        btn.disabled = false;
        btn.innerHTML = txt;
        isSubmitting = false;
    });

    // Sincronizar al recuperar conexión
    const sincronizar = async () => {
        if (!navigator.onLine || isSubmitting) return;
        const db = await getDB();
        const tx = db.transaction('pendientes', 'readonly');
        const pendientes = [];
        tx.objectStore('pendientes').openCursor().onsuccess = e => {
            const cursor = e.target.result;
            if (cursor) { pendientes.push(cursor.value); cursor.continue(); }
        };
        await tx.complete;

        for (const p of pendientes) {
            if (await enviar(p.data)) {
                const d = await getDB();
                const t = d.transaction('pendientes', 'readwrite');
                t.objectStore('pendientes').delete(p.key);
                await t.complete;
            } else break;
        }
        if (pendientes.length > 0) notificar(`✅ ${pendientes.length} sincronizado(s)`);
    };

    window.addEventListener('online', sincronizar);
    // Intentar al cargar (si hay conexión)
    if (navigator.onLine) setTimeout(sincronizar, 1000);
});