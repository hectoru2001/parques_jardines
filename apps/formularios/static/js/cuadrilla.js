document.addEventListener('DOMContentLoaded', function () {
    // Seleccionamos el contenedor
    const contenedor = document.querySelector('.logica-seleccion');
    
    if (!contenedor) return; 

    const checkboxes = contenedor.querySelectorAll('input[type="checkbox"]');

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function () {
            if (this.checked) {
                checkboxes.forEach(other => {
                    if (other !== this) {
                        other.checked = false;
                    }
                });
            }
        });
    });
});

function ValidaSuperficieAtendida() {
    let v1 = parseInt(document.getElementById("id_cesped_cortado_m2").value) || 0;
    let v2 = parseInt(document.getElementById("id_deshierbe_m2").value) || 0;
    let v3 = parseInt(document.getElementById("id_papeleo_m2").value) || 0;

    let comparacion = parseInt(document.getElementById("id_superficie_atendida_m2").value) || 0;
    let SumaCampos = v1 + v2 + v3;

    document.getElementById("id_cesped_cortado_m2").classList.remove("is-invalid");
    document.getElementById("id_deshierbe_m2").classList.remove("is-invalid");
    document.getElementById("id_papeleo_m2").classList.remove("is-invalid");

    if (SumaCampos > comparacion) {
        alert("La suma (" + SumaCampos + ") no puede ser mayor que la superficie total (" + comparacion + ").");

        document.getElementById("id_cesped_cortado_m2").classList.add("is-invalid");
        document.getElementById("id_deshierbe_m2").classList.add("is-invalid");
        document.getElementById("id_papeleo_m2").classList.add("is-invalid");
        return false;
    }
    return true;
}

