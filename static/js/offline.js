// offline.js - Guardado offline para Reporte Riego Chamizal (con API JSON)

document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form[data-form-name="riego-chamizal"]');
    if (!form) return;

    // 👇 Usa la URL de tu API (ajusta si es diferente)
    const API_URL = '/formularios/api/riego-chamizal/';
    let isSubmitting = false;

    // --- IndexedDB ---
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

    // --- Enviar al backend como JSON ---
    async function enviarAlBackend(datos) {
        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    // No necesitas CSRF porque usas @csrf_exempt
                },
                body: JSON.stringify(datos)
            });

            const result = await response.json();
            if (response.ok && result.status === 'ok') {
                return true;
            } else {
                console.warn('Error de validación:', result.errors || result.message);
                return false;
            }
        } catch (err) {
            console.warn('Error de red:', err);
            return false;
        }
    }

    // --- Sincronización automática ---
    async function sincronizarPendientes() {
        if (!navigator.onLine || isSubmitting) return;

        const pendientes = await obtenerPendientes();
        if (pendientes.length === 0) return;

        isSubmitting = true;
        for (const item of pendientes) {
            const exito = await enviarAlBackend(item.datos);
            if (exito) {
                await eliminarPendiente(item.id);
                console.log('✅ Registro offline sincronizado:', item.id);
            } else {
                break; // Detener si falla uno
            }
        }
        isSubmitting = false;

        if (pendientes.length > 0) {
            mostrarNotificacion(`✅ ${pendientes.length} registro(s) sincronizado(s)`);
        }
    }

    // --- Notificación suave ---
    function mostrarNotificacion(mensaje) {
        let notif = document.getElementById('offline-notif');
        if (!notif) {
            notif = document.createElement('div');
            notif.id = 'offline-notif';
            notif.style.cssText = `
                position: fixed;
                bottom: 20px;
                left: 50%;
                transform: translateX(-50%);
                background: #28a745;
                color: white;
                padding: 12px 20px;
                border-radius: 8px;
                font-size: 16px;
                z-index: 10000;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            `;
            document.body.appendChild(notif);
        }
        notif.textContent = mensaje;
        notif.style.display = 'block';
        setTimeout(() => notif.style.display = 'none', 3000);
    }

    // --- Intercepta el envío del formulario ---
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        if (isSubmitting) return;

        // Obtener datos del formulario como objeto plano
        const formData = new FormData(form);
        const datos = Object.fromEntries(formData.entries());

        isSubmitting = true;

        if (navigator.onLine) {
            const exito = await enviarAlBackend(datos);
            if (exito) {
                // Redirigir al menú o mostrar éxito
                window.location.href = '/menu/'; // o donde quieras ir tras guardar
            } else {
                await guardarPendiente(datos);
                mostrarNotificacion('⚠️ Guardado localmente. Se enviará cuando haya conexión.');
            }
        } else {
            await guardarPendiente(datos);
            mostrarNotificacion('📱 Sin conexión. Guardado localmente.');
            // Opcional: form.reset(); // No lo hago porque quizás quieras corregir y reenviar
        }

        isSubmitting = false;
    });

    // --- Sincronizar al cargar y al recuperar conexión ---
    window.addEventListener('load', sincronizarPendientes);
    window.addEventListener('online', sincronizarPendientes);
});