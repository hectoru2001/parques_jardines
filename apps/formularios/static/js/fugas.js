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