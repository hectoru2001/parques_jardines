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

document.getElementById("print-selected").addEventListener("click", function() {
    let ids = [];
    document.querySelectorAll(".reporte-checkbox:checked").forEach(cb => {
        ids.push(cb.value);
    });

    if (ids.length === 0) {
        showModal("Selecciona al menos un reporte.", "alert");
        return;
    }
    if (ids.length > 4) {
        showModal("Solo puedes imprimir máximo 4 reportes por hoja.", "alert");
        return;
    }

    window.open(`/formularios/fuentes/reporte/pdf-multiple/${ids.join(",")}`, "_blank");
});

function ValidaSuperficieAtendida() {
    let v1 = parseInt(document.getElementById("id_limpieza_papeleo_m2").value) || 0;
    let comparacion = parseInt(document.getElementById("id_superficie_atendida_m2").value) || 0;

    document.getElementById("id_limpieza_papeleo_m2").classList.remove("is-invalid");

    if (v1 > comparacion) {
        showModal(`La limpieza de papeleo no puede ser mayor que la superficie total.`, `alert`);

        document.getElementById("id_limpieza_papeleo_m2").classList.add("is-invalid");
        return false;
    }
    return true;
}


