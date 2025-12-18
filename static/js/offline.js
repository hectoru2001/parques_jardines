document.addEventListener('DOMContentLoaded', function() {

    // --- Funciones de almacenamiento offline ---
    function guardarPendiente(formName, datos) {
        const key = `${formName}_pendientes`;
        const pendientes = JSON.parse(localStorage.getItem(key) || '[]');
        pendientes.push({ datos, ts: Date.now() });
        localStorage.setItem(key, JSON.stringify(pendientes));
        actualizarBotonSincronizar(formName);
    }

    function obtenerPendientes(formName) {
        const key = `${formName}_pendientes`;
        return JSON.parse(localStorage.getItem(key) || '[]');
    }

    function limpiarPendientes(formName) {
        const key = `${formName}_pendientes`;
        localStorage.removeItem(key);
        actualizarBotonSincronizar(formName);
    }

    function actualizarBotonSincronizar(formName) {
        const btnSincronizar = document.getElementById(`btnSincronizar`);
        const spanContador = document.getElementById(`contador-pendientes`);
        if (!btnSincronizar || !spanContador) return;

        const cantidad = obtenerPendientes(formName).length;
        spanContador.textContent = cantidad;
        btnSincronizar.style.display = cantidad > 0 ? 'inline-block' : 'none';
    }

    // --- Función de envío (POST) ---
    function enviar(formName, datos) {
        return new Promise((resolve) => {
            const xhr = new XMLHttpRequest();
            xhr.open('POST', `/formularios/api/${formName}/`, true);
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

    // --- Sincronizar pendientes ---
    async function sincronizarPendientes(formName) {
        const btnSincronizar = document.getElementById(`btnSincronizar`);
        if (!btnSincronizar || btnSincronizar.disabled) return;

        const pendientes = obtenerPendientes(formName);
        if (pendientes.length === 0) return;

        btnSincronizar.disabled = true;
        const originalText = btnSincronizar.innerHTML;
        btnSincronizar.innerHTML = `📤 Subiendo ${pendientes.length}...`;

        let todosExitosos = true;
        for (const item of pendientes) {
            const exito = await enviar(formName, item.datos);
            if (!exito) {
                todosExitosos = false;
                showModal('Error al subir un registro. Verifica la conexión e intenta de nuevo. ⚠️', 'error');
                break;
            }
        }

        if (todosExitosos) {
            limpiarPendientes(formName);
            showModal('Todos los registros se guardaron en el servidor. ✅', 'success');
            const redirectUrl = document.querySelector(`form[data-form-name="${formName}"]`)?.dataset.redirect;
            if (redirectUrl) window.location.href = redirectUrl;
        }

        btnSincronizar.innerHTML = originalText;
        btnSincronizar.disabled = false;
        actualizarBotonSincronizar(formName);
    }

    // --- Inicializar formularios ---
    document.querySelectorAll('form[data-form-name]').forEach(form => {
        const formName = form.dataset.formName;
        const btnSincronizar = document.getElementById(`btnSincronizar`);
        const spanContador = document.getElementById(`contador-pendientes`);

        // Interceptar submit solo si no hay conexión
        form.addEventListener('submit', async function(e) {
            if (navigator.onLine) return; // flujo normal

            e.preventDefault();
            e.stopPropagation();

            const formData = new FormData(form);
            const datos = {};

            async function fileToBase64(file) {
                return new Promise(resolve => {
                    const reader = new FileReader();
                    reader.onload = () => resolve(reader.result); // Base64 lista
                    reader.readAsDataURL(file);
                });
            }

            for (const [k, v] of formData.entries()) {
                if (v instanceof File && v.size > 0) {
                    // Convertir imagen a Base64
                    datos[k] = await fileToBase64(v);
                } else {
                    datos[k] = v;
                }
            }

            guardarPendiente(formName, datos);
            showModal('Sin conexión. Reporte guardado en el dispositivo. Usa el botón verde para guardar los reportes pendientes.', 'alert');
            //form.reset();
        });


        // Botón de sincronización
        if (btnSincronizar) {
            btnSincronizar.addEventListener('click', () => sincronizarPendientes(formName));
        }

        // Inicializar contador al cargar
        actualizarBotonSincronizar(formName);
    });
});
