document.addEventListener("DOMContentLoaded", function() {
    const reportCards = document.querySelectorAll('.report-card');
    
    // Configuración del modal para vista previa
    const previewButtons = document.querySelectorAll('.preview-btn');
    const imageModal = new bootstrap.Modal(document.getElementById('imageModal'));
    const modalImage = document.getElementById('modalImage');
    const modalTitle = document.getElementById('imageModalLabel');
    
    previewButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Obtener la URL de la imagen y el título
            const imageUrl = this.getAttribute('href');
            const title = this.getAttribute('data-title');
            
            // Establecer la imagen y el título en el modal
            modalImage.src = imageUrl;
            modalImage.alt = title;
            modalTitle.textContent = title;
            
            // Mostrar el modal
            imageModal.show();
        });
    });
    
    // Efectos de hover mejorados para dispositivos táctiles
    let touchTimeout;
    
    reportCards.forEach(card => {
        card.addEventListener('touchstart', function() {
            touchTimeout = setTimeout(() => {
                this.classList.add('hover-effect');
            }, 200);
        });
        
        card.addEventListener('touchend', function() {
            clearTimeout(touchTimeout);
            this.classList.remove('hover-effect');
        });
    });
});