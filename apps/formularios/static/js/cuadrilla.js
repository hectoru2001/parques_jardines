function ValidaSuperficieAtendida() {
    const campos = [
        "id_cesped_cortado_m2",
        "id_deshierbe_m2",
    ];

    campos.forEach(id => document.getElementById(id).classList.remove("is-invalid"));

    const comparacion = parseInt(document.getElementById("id_superficie_atendida_m2").value) || 0;
    let hayError = false;

    campos.forEach(id => {
        const valor = parseInt(document.getElementById(id).value) || 0;
        
        if (valor > comparacion) {
            document.getElementById(id).classList.add("is-invalid");
            hayError = true;
        }
    });

    if (hayError) {
        showModal(`Cada campo debe ser menor o igual que la superficie total (${comparacion}).`, "alert");
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





