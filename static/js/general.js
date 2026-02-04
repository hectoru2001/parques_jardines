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

function toggleFecha() {
    const filtro = document.getElementById('filtro-select').value;
    const queryInput = document.getElementById('query-input');
    const fechaInicio = document.getElementById('fecha-inicio');
    const fechaFin = document.getElementById('fecha-fin');

    if (filtro === 'fecha') {
        queryInput.classList.add('d-none');
        fechaInicio.classList.remove('d-none');
        fechaFin.classList.remove('d-none');
    } else {
        queryInput.classList.remove('d-none');
        fechaInicio.classList.add('d-none');
        fechaFin.classList.add('d-none');
    }
}

function seleccionarDiaAuto() {
    const inputFecha = document.getElementById('id_fecha');
    const selectDia = document.getElementById('id_dia');

    if (!inputFecha.value) {
        selectDia.value = "";
        return;
    }

    const [year, month, day] = inputFecha.value.split('-').map(Number);

    // Fecha LOCAL — no usar UTC aquí
    const fecha = new Date(year, month - 1, day);

    const dias = [
        "Domingo", "Lunes", "Martes",
        "Miércoles", "Jueves", "Viernes", "Sábado"
    ];

    selectDia.value = dias[fecha.getDay()];
}



document.addEventListener('DOMContentLoaded', function () {
    const contenedor = document.querySelector('.logica-seleccion');
    const formulario = contenedor ? contenedor.closest('form') : null;
    const inputsNumericos = document.querySelectorAll('input[type="number"]');
    const checkBoxes = document.getElementById('list-checkboxes');

    const esSupervisor = window.ES_SUPERVISOR === "true";
    const inputFecha = document.getElementById("id_fecha");

        if (!inputFecha) return;

    // =========================
    // FECHA (FIX CHROME)
    // =========================
    const hoyDate = new Date();
    hoyDate.setHours(0, 0, 0, 0);
    const hoy = hoyDate.toISOString().split("T")[0];

    if (!esSupervisor) {
        inputFecha.min = hoy;

        let timeout;

        inputFecha.addEventListener("input", function () {
            clearTimeout(timeout);

            timeout = setTimeout(() => {
                if (!this.value) return;

                const fechaSeleccionada = new Date(this.value);

                // Chrome dispara eventos con fechas inválidas
                if (isNaN(fechaSeleccionada)) return;

                fechaSeleccionada.setHours(0, 0, 0, 0);

                if (fechaSeleccionada < hoyDate) {
                    showModal("La fecha no puede ser anterior a hoy.");
                    this.value = hoy;
                    return;
                }

                // ✅ Solo cuando la fecha es válida
                seleccionarDiaAuto();

            }, 120);
        });
    }

    toggleFecha();


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

    function previewImage(input, previewId) {
        const preview = document.getElementById(previewId);
        if (input.files && input.files[0]) {
            const reader = new FileReader();
            reader.onload = function(e) {
                preview.src = e.target.result;
                preview.style.display = 'block';
            }
            reader.readAsDataURL(input.files[0]);
        } else {
            preview.src = '';
            preview.style.display = 'none';
        }
    }

    const fotoAntesInput = document.getElementById('id_foto_antes');
    const fotoDespuesInput = document.getElementById('id_foto_despues');

    if (fotoAntesInput) {
        previewImage(fotoAntesInput, 'preview_antes'); // muestra la imagen existente al cargar
        fotoAntesInput.addEventListener('change', function() {
            previewImage(this, 'preview_antes');
        });
    }

    if (fotoDespuesInput) {
        previewImage(fotoDespuesInput, 'preview_despues'); // muestra la imagen existente al cargar
        fotoDespuesInput.addEventListener('change', function() {
            previewImage(this, 'preview_despues');
        });
    }
});
