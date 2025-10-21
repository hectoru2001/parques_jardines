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
        // Usamos el modal reutilizable
        showModal(`La suma de los campos cesped cortado, deshierbe y papeleo no puede ser mayor que la superficie total.`, `alert`);

        document.getElementById("id_cesped_cortado_m2").classList.add("is-invalid");
        document.getElementById("id_deshierbe_m2").classList.add("is-invalid");
        document.getElementById("id_papeleo_m2").classList.add("is-invalid");

        return false;
    }
    return true;
}

document.querySelector('form').addEventListener('submit', function(e){
    if(!ValidaSuperficieAtendida()){
        e.preventDefault();
        e.stopImmediatePropagation();
    }
});





