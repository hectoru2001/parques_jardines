const chbxTDiario = document.getElementById("id_trabajo_ciudadania");
const inputTDiario = document.getElementById("id_folio_pac");
const divOperativo = document.getElementById("operativo-comentarios")

document.addEventListener('DOMContentLoaded', function () {
    // Seleccionamos todos los checkboxes involucrados
    const checkboxes = document.querySelectorAll('input[type="checkbox"][name^="trabajo_"], input[type="checkbox"][name="operativo_especial"]');
    ValidaTrabajoDiario();
    inputTDiario.disabled = true;

    // Recorremos los checkboxes y les agregamos un evento change para solo permitir uno seleccionado
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function () {
            if (this.checked) {
                // Desmarcar todos los demás checkboxes
                checkboxes.forEach(other => {
                    if (other !== this) {
                        other.checked = false;
                    }
                });
            }
            ValidaTrabajoDiario();
        });
    });
});

// Se agrega el evento a la los checkboxes dentro del div con id valida-pac
document.querySelectorAll('#valida-pac input[type="checkbox"]').forEach(checkbox => {
    checkbox.addEventListener('change', ValidaTrabajoDiario);
});

document.querySelector('form').addEventListener('submit', function(e) {
    if(!ValidarCheckboxTrabajo()){
        e.preventDefault();
        showModal("Debes seleccionar al menos un trabajo", "alert");
    }
});


// Desactiva o activa el campo folio PAC según el checkbox trabajo_ciudadania
// Desactiva o activa el campo folio PAC según el checkbox trabajo_ciudadania
function ValidaTrabajoDiario() {
    // Validación del folio PAC (tu lógica original)
    if (chbxTDiario.checked) {
        inputTDiario.required = true;
        inputTDiario.disabled = false;
    } else {
        inputTDiario.required = false;
        inputTDiario.disabled = true;
    }

    // Mostrar u ocultar un div según un checkbox 
    const chkOperativo = document.getElementById('id_operativo_especial');
    const divOperativo = document.getElementById('operativo-comentarios');

    if (chkOperativo && divOperativo) {
        if (chkOperativo.checked) {
            // Mostrar y habilitar los campos
            divOperativo.style.display = 'block';
            divOperativo.querySelectorAll('input, select, textarea, button').forEach(el => {
                el.disabled = false;
            });
        } else {
            // Ocultar y deshabilitar los campos
            divOperativo.style.display = 'none';
            divOperativo.querySelectorAll('input, select, textarea, button').forEach(el => {
                el.disabled = true;
            });
        }
    }
}


function ValidarCheckboxTrabajo() {
    // Seleccionamos los checkboxes del grupo
    const checkboxes = document.querySelectorAll('input[type="checkbox"][name^="trabajo_"], input[type="checkbox"][name="operativo_especial"]');
    
    // Verificamos si alguno está marcado
    const algunoMarcado = Array.from(checkboxes).some(cb => cb.checked);

    // Marcar en rojo si no hay ninguno seleccionado
    checkboxes.forEach(cb => {
        if (!algunoMarcado) {
            cb.classList.add("is-invalid");
        } else {
            cb.classList.remove("is-invalid");
        }
    });

    return algunoMarcado;
}

