function showModal(message, type) {
    let icon;
    switch(type) {
        case 'success': icon = 'success'; break;
        case 'error':   icon = 'error'; break;
        case 'alert':   icon = 'warning'; break;
        default:        icon = 'info';
    }

    Swal.fire({
        text: message,
        icon: icon,
        confirmButtonText: 'Aceptar',
        customClass: {
            popup: 'modal-popup',
            title: 'modal-title',
            content: 'modal-content',
            confirmButton: 'modal-btn'
        },
        backdrop: true
    });
}



document.addEventListener('DOMContentLoaded', function () {
    const contenedor = document.querySelector('.logica-seleccion');
    const formulario = contenedor ? contenedor.closest('form') : null;
    const inputsNumericos = document.querySelectorAll('input[type="number"]');
    const checkBoxes = document.getElementById('list-checkboxes');

    /*inputsNumericos.forEach(input => {
        input.value = ''; // Se queda vacío pero sigue siendo requerido
    });*/

    if (formulario) {
        formulario.addEventListener('submit', function (e) {
            const algunoSeleccionado = Array.from(checkBoxes.querySelectorAll('input[type="checkbox"]')).some(cb => cb.checked);
            if (!algunoSeleccionado) {
                e.preventDefault();
                showModal('Debes seleccionar al menos una opción antes de continuar.', 'alert');
                checkBoxes.classList.add('div-invalid');
                return false;
            }
        });
    }

    if (typeof inputTDiario !== 'undefined') {
        inputTDiario.disabled = true;
    }

    if (contenedor) {
        const checkboxes = contenedor.querySelectorAll('input[type="checkbox"]');

        // Solo permitir seleccionar uno a la vez
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
    }
});
