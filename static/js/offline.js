document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form[data-form-name="riego-chamizal"]');
    const submitBtn = form?.querySelector('button[type="submit"]');
    if (!form || !submitBtn) return;

    const API_URL = '/formularios/api/riego-chamizal/';
    let isSubmitting = false;

    // --- IndexedDB (igual que antes) ---
    const openDB = () => {
        return new Promise((resolve, reject) => {
            const req = indexedDB.open('RiegoOfflineDB', 1);
            req.onerror = () => reject(req.error);
            req.onsuccess = () => resolve(req.result);
            req.onupgradeneeded = (e) => {
                const db = e.target.result;
                if (!db.objectStoreNames.contains('pendientes')) {
                    db.createObjectStore('pendientes', { keyPath: 'id', autoIncrement: true });
                }
            };
        });
    };

    const guardarPendiente = async (datos) => {
        const db = await openDB();
        const tx = db.transaction('pendientes', 'readwrite');
        const store = tx.objectStore('pendientes');
        await store.add({ datos, timestamp: Date.now() });
        await tx.complete;
    };

    const obtenerPendientes = async () => {
        const db = await openDB();
        const tx = db.transaction('pendientes', 'readonly');
        const store = tx.objectStore('pendientes');
        return new Promise(resolve => {
            const pendientes = [];
            store.openCursor().onsuccess = (e) => {
                const cursor = e.target.result;
                if (cursor) {
                    pendientes.push(cursor.value);
                    cursor.continue();
                } else {
                    resolve(pendientes);
                }
            };
        });
    };

    const eliminarPendiente = async (id) => {
        const db = await openDB();
        const tx = db.transaction('pendientes', 'readwrite');
        const store = tx.objectStore('pendientes');
        store.delete(id);
        await tx.complete;
    };

    async function enviarAlBackend(datos) {
        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(datos)
            });
            const result = await response.json();
            return response.ok && result.status === 'ok';
        } catch (err) {
            console.warn('Error de red:', err);
            return false;
        }
    }

    function mostrarNotificacion(mensaje) {
        let notif = document.getElementById('offline-notif');
        if (!notif) {
            notif = document.createElement('div');
            notif.id = 'offline-notif';
            notif.style.cssText = `
                position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%);
                background: #28a745; color: white; padding: 12px 20px;
                border-radius: 8px; font-size: 16px; z-index: 10000;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2); text-align: center;
            `;
            document.body.appendChild(notif);
        }
        notif.textContent = mensaje;
        notif.style.display = 'block';
        setTimeout(() => notif.style.display = 'none', 3000);
    }

    // ✅ NUEVO: Evita doble envío y comportamiento nativo
    async function manejarSubmit(e) {
        e.preventDefault();
        e.stopPropagation(); // ← Evita burbuja de eventos

        // Si ya se está procesando, ignora
        if (isSubmitting) return;

        // Desactiva el botón visualmente (mejor UX en móvil)
        const originalText = submitBtn.innerHTML;
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span>Guardando...</span>';

        const formData = new FormData(form);
        const datos = Object.fromEntries(formData.entries());

        isSubmitting = true;

        if (navigator.onLine) {
            const exito = await enviarAlBackend(datos);
            if (exito) {
                window.location.href = '/menu/';
            } else {
                await guardarPendiente(datos);
                mostrarNotificacion('⚠️ Guardado localmente. Se enviará cuando haya conexión.');
                // Restaurar botón
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalText;
            }
        } else {
            await guardarPendiente(datos);
            mostrarNotificacion('📱 Sin conexión. Guardado localmente.');
            // Opcional: no limpiar el formulario para que puedan corregir
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalText;
        }

        isSubmitting = false;
    }

    // ✅ Escuchar SOLO el evento 'submit' del formulario (no 'click' del botón)
    form.addEventListener('submit', manejarSubmit);

    // ✅ Opcional: prevenir toques múltiples en el botón (extra para iOS)
    if (submitBtn) {
        let lastTouch = 0;
        submitBtn.addEventListener('touchstart', (e) => {
            const now = Date.now();
            if (now - lastTouch <= 500) {
                e.preventDefault();
                return false;
            }
            lastTouch = now;
        });
    }

    // Sincronización automática
    async function sincronizarPendientes() {
        if (!navigator.onLine || isSubmitting) return;
        const pendientes = await obtenerPendientes();
        if (pendientes.length === 0) return;

        isSubmitting = true;
        for (const item of pendientes) {
            const exito = await enviarAlBackend(item.datos);
            if (exito) {
                await eliminarPendiente(item.id);
            } else {
                break;
            }
        }
        isSubmitting = false;

        if (pendientes.length > 0) {
            mostrarNotificacion(`✅ ${pendientes.length} registro(s) sincronizado(s)`);
        }
    }

    window.addEventListener('load', sincronizarPendientes);
    window.addEventListener('online', sincronizarPendientes);
});