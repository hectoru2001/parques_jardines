// ------------------- Inicialización Dexie -------------------
const db = new Dexie("FormulariosOffline");

// Versión 1 de la DB
db.version(1).stores({
    formularios: "++id, formName, timestamp"
});

// ------------------- Funciones -------------------

// Guardar formulario offline
async function saveFormOffline(formName, data) {
    await db.formularios.add({ formName, data, timestamp: new Date() });
    console.log(`✔ ${formName} guardado offline`);
    await showPendingForms();
}

// Mostrar formularios pendientes en consola
async function showPendingForms() {
    const items = await db.formularios.toArray();
    console.clear();
    if (items.length === 0) {
        console.log("✅ No hay formularios pendientes");
        return;
    }
    console.log("📋 Formularios pendientes de sincronizar:");
    items.forEach(item => {
        console.log(`- ${item.formName}, guardado el ${item.timestamp}`, item.data);
    });
}

// Borrar un formulario por ID
async function deleteFormById(id) {
    await db.formularios.delete(id);
    console.log(`🗑️ Formulario con id ${id} borrado tras sincronización exitosa`);
}

// ------------------- Sincronización -------------------
async function syncForms() {
    if (!navigator.onLine) return; // solo si hay conexión

    const items = await db.formularios.toArray();

    for (let item of items) {
        const endpoint = `/formularios/api/${item.formName}/`;
        try {
            const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            const response = await fetch(endpoint, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken
                },
                body: JSON.stringify(item.data),
            });

            if (response.ok) {
                console.log(`✅ ${item.formName} sincronizado`);
                // Borrar solo el formulario que se sincronizó
                await deleteFormById(item.id);
            } else {
                console.log(`⚠️ Error de servidor al sincronizar ${item.formName}. Datos quedan guardados offline.`);
            }
        } catch (err) {
            console.log(`📡 No se pudo conectar al servidor para ${item.formName}. Datos siguen offline.`, err);
        }
    }
}

// ------------------- Manejo de formularios -------------------
document.addEventListener("DOMContentLoaded", () => {
    const forms = document.querySelectorAll("form[data-form-name]");

    forms.forEach(form => {
        form.addEventListener("submit", async (event) => {
            event.preventDefault();

            const formName = form.dataset.formName;
            const formData = {};

            form.querySelectorAll("input, select, textarea").forEach(field => {
                const name = field.name;
                if (!name || name === "csrfmiddlewaretoken") return;

                if (field.type === "checkbox") formData[name] = field.checked;
                else if (field.type === "number") formData[name] = field.value ? Number(field.value) : null;
                else formData[name] = field.value;
            });

            // Guardar offline
            await saveFormOffline(formName, formData);

            // Intentar sincronizar si hay conexión
            if (navigator.onLine) await syncForms();

            form.reset();
        });
    });

    // Sincronizar automáticamente al reconectarse
    window.addEventListener("online", () => {
        console.log("🌐 Conexión restablecida → sincronizando formularios pendientes...");
        syncForms();
    });
});

