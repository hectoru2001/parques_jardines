document.addEventListener('DOMContentLoaded', function() {
    const API_URL = '/formularios/api/riego-chamizal/';
    const btnGuardar = document.getElementById('btn-guardar-offline');
    const btnSincronizar = document.getElementById('btn-sincronizar-pendientes');
    const spanContador = document.getElementById('contador-pendientes');
    
    if (!btnGuardar || !btnSincronizar || !spanContador) {
        console.error('❌ Faltan elementos en el DOM');
        return;
    }

    let isSubmitting = false;

    // --- Almacenamiento ---
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

    // ✅ Actualiza visibilidad y contador
    function actualizarBotonSincronizar() {
        const pendientes = obtenerPendientes();
        const cantidad = pendientes.length;
        console.log(pendientes, cantidad)
        if (cantidad > 0) {
            spanContador.textContent = cantidad;
            btnSincronizar.style.display = 'block';
        } else {
            btnSincronizar.style.display = 'none';
        }
    }

    // --- Enviar un registro ---
    function enviar(datos) {
        return new Promise((resolve) => {
            const xhr = new XMLHttpRequest();
            xhr.open('POST', API_URL, true);
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

    // --- Sincronizar manualmente ---
    async function sincronizarPendientes() {
        if (isSubmitting) return;
        isSubmitting = true;

        const pendientes = obtenerPendientes();
        if (pendientes.length === 0) {
            actualizarBotonSincronizar();
            isSubmitting = false;
            return;
        }

        // Cambiar texto del botón
        const originalText = btnSincronizar.innerHTML;
        btnSincronizar.innerHTML = `📤 Subiendo ${pendientes.length}...`;
        btnSincronizar.disabled = true;

        let exitos = 0;
        for (const item of pendientes) {
            const exito = await enviar(item.datos);
            if (exito) {
                exitos++;
            } else {
                alert(`⚠️ Error al subir registro #${exitos + 1}. Deteniendo.`);
                break;
            }
        }

        if (exitos === pendientes.length) {
            limpiarPendientes();
            alert('✅ Todos los registros se guardaron en el servidor.');
        } else {
            // Actualizar contador con los que quedaron
            actualizarBotonSincronizar();
        }

        btnSincronizar.innerHTML = originalText;
        btnSincronizar.disabled = false;
        isSubmitting = false;
    }

    // --- Guardar formulario principal ---
    btnGuardar.addEventListener('click', async function() {
        if (isSubmitting) return;

        const form = document.querySelector('form[data-form-name="riego-chamizal"]');
        const datos = {};
        new FormData(form).forEach((v, k) => datos[k] = v);

        if (navigator.onLine) {
            isSubmitting = true;
            btnGuardar.disabled = true;
            btnGuardar.innerHTML = 'Guardando...';

            const exito = await enviar(datos);
            isSubmitting = false;
            btnGuardar.disabled = false;
            btnGuardar.innerHTML = 'Guardar Reporte';

            if (exito) {
                window.location.href = '/menu/';
            } else {
                guardarPendiente(datos);
                alert('⚠️ Guardado localmente. Usa el botón verde para subir después.');
            }
        } else {
            guardarPendiente(datos);
            alert('📱 Sin conexión. Guardado localmente. Usa el botón verde para subir después.');
        }
        form.clear()
    });

    // --- Botón de sincronización ---
    btnSincronizar.addEventListener('click', sincronizarPendientes);

    // --- Inicializar al cargar ---
    actualizarBotonSincronizar();
});