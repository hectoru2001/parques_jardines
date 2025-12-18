document.addEventListener('DOMContentLoaded', function() {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    })
})
document.getElementById("select-all").addEventListener("change", function() {
    document.querySelectorAll(".reporte-checkbox").forEach(cb => {
        cb.checked = this.checked;
    });
});

document.getElementById("print-selected-riego-pipas").addEventListener("click", function() {
    let ids = [];
    document.querySelectorAll(".reporte-checkbox:checked").forEach(cb => {
        ids.push(cb.value);
    });

    if (ids.length === 0) {
        alert("Selecciona al menos un reporte.");
        return;
    }
    if (ids.length > 2) {
        alert("Solo puedes imprimir máximo 4 reportes por hoja.");
        return;
    }

    window.open(`/formularios/riego_pipas/reporte/pdf-multiple/${ids.join(",")}`, "_blank");
});