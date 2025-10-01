document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form[data-form-name="riego-chamizal"]');
    const btnGuardar = document.getElementById('btn-guardar-offline');
    const btnSincronizar = document.getElementById('btn-sincronizar-pendientes');
    const spanContador = document.getElementById('contador-pendientes');

    // Si no hay botón de sincronización, no hay offline
    if (!btnSincronizar || !spanContador) return;

    let isSubmitting = false;

    // --- Almacenamiento offline ---
    function guardarPendiente(datos) {
        const pendientes = JSON.parse(localStorage.getItem('riego_pendientes') || '[]');
        pendientes.push({ datos, ts: Date.now() });
        localStorage.setItem('riego_pendientes', JSON.stringify(pendientes));
        actualizarBotonSincronizar();
    }

    function obtenerPendientes() {
        return JSON.parse(localStorage.getItem('riego_pendientes') || '[]');
    }

    function limpiarPendientes() {
        localStorage.removeItem('riego_pendientes');
        actualizarBotonSincronizar();
    }

    function actualizarBotonSincronizar() {
        const cantidad = obtenerPendientes().length;
        if (cantidad > 0) {
            spanContador.textContent = cantidad;
            btnSincronizar.style.display = 'block';
        } else {
            btnSincronizar.style.display = 'none';
        }
    }

    // --- API para sincronizar offline ---
    function enviar(datos) {
        return new Promise((resolve) => {
            const xhr = new XMLHttpRequest();
            xhr.open('POST', '/formularios/api/riego-chamizal/', true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4) {
                    const ok = xhr.status >= 200 && xhr.status < 300;
                    try {
                        const resp = JSON.parse(xhr.responseText || '{}');
                        resolve(ok && resp.status === 'ok');
                    } catch {
                        resolve(false);
                    }
                }
            };
            xhr.send(JSON.stringify(datos));
        });
    }

    // --- Sincronizar pendientes (solo offline) ---
    async function sincronizarPendientes() {
        if (isSubmitting) return;
        isSubmitting = true;

        const pendientes = obtenerPendientes();
        if (pendientes.length === 0) {
            actualizarBotonSincronizar();
            isSubmitting = false;
            return;
        }

        const originalText = btnSincronizar.innerHTML;
        btnSincronizar.innerHTML = `📤 Subiendo ${pendientes.length}...`;
        btnSincronizar.disabled = true;

        let todosExitosos = true;
        for (const item of pendientes) {
            const exito = await enviar(item.datos);
            if (!exito) {
                todosExitosos = false;
                alert('⚠️ Error al subir un registro. Inténtalo de nuevo.');
                break;
            }
        }

        if (todosExitosos) {
            limpiarPendientes();
            alert('✅ Todos los registros se guardaron en el servidor.');
            window.location.href = "/formularios/riego_chamizal/lista/"
        } else {
            actualizarBotonSincronizar();
        }

        btnSincronizar.innerHTML = originalText;
        btnSincronizar.disabled = false;
        isSubmitting = false;
    }

    // --- Intercepta el submit SOLO si no hay conexión ---
    if (form) {
        form.addEventListener('submit', function(e) {
            // Si hay conexión, deja que Django maneje el submit (no hacer nada)
            if (navigator.onLine) {
                return; // ✅ Flujo normal de Django
            }

            // Si NO hay conexión, prevenir el submit y guardar offline
            e.preventDefault();
            e.stopPropagation();

            const datos = {};
            new FormData(form).forEach((v, k) => datos[k] = v);

            guardarPendiente(datos);
            alert('📱 Sin conexión. Guardado localmente. Usa el botón verde para subir después.');
        });
    }

    // --- Botón de sincronización ---
    if (btnSincronizar) {
        btnSincronizar.addEventListener('click', sincronizarPendientes);
    }

    // --- Inicializar botón al cargar ---
    actualizarBotonSincronizar();
});