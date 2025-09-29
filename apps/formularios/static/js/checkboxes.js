document.addEventListener('DOMContentLoaded', function () {
    // Seleccionamos todos los checkboxes involucrados
    const checkboxes = document.querySelectorAll('input[type="checkbox"][name^="trabajo_"], input[type="checkbox"][name="operativo_especial"]');

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
        });
    });
});
