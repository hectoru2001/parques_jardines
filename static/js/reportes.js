document.addEventListener('DOMContentLoaded', function() {
    const reporteModal = document.getElementById('reporteModal');
    if (reporteModal) {
        reporteModal.addEventListener('show.bs.modal', function(event) {
            const trigger = event.relatedTarget;
            const reporteId = trigger.getAttribute('data-id');
            const tipo = trigger.getAttribute('data-tipo');

            const body = document.getElementById('modal-body-content');
            body.innerHTML = '<div class="text-center p-3 text-muted">Cargando...</div>';

            fetch(`/formularios/reportes/modal/${tipo}/${reporteId}/`)
                .then(res => res.text())
                .then(html => {
                    body.innerHTML = html;
                })
                .catch(err => {
                    console.error(err);
                    body.innerHTML = '<p class="text-danger">Error al cargar los datos.</p>';
                });
        });
    }
});
