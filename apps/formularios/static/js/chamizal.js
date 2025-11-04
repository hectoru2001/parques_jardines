function ValidaSuperficieAtendida() {
    const campos = [
        "id_cesped_cortado_m2",
        "id_deshierbe_m2",
    ];

    // Limpiar clases de error
    campos.forEach(id => document.getElementById(id).classList.remove("is-invalid"));

    // Obtener valores de los campos
    let suma = campos.reduce((acc, id) => {
        return acc + (parseInt(document.getElementById(id).value) || 0);
    }, 0);

    const comparacion = parseInt(document.getElementById("id_superficie_atendida_m2").value) || 0;

    if (suma > comparacion) {
        // Mostrar modal de error
        showModal(`La suma de los campos no puede ser mayor que la superficie total (${comparacion}).`, "alert");

        // Marcar campos inválidos
        campos.forEach(id => document.getElementById(id).classList.add("is-invalid"));
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