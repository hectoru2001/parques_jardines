document.addEventListener("DOMContentLoaded", function() {
    // Elementos del DOM
    const searchInput = document.getElementById('reportSearch');
    const filterButtons = document.querySelectorAll('.filter-btn');
    const reportCards = document.querySelectorAll('.report-card');
    
    // Filtrado por búsqueda
    searchInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase();
        
        reportCards.forEach(card => {
            const title = card.querySelector('h3').textContent.toLowerCase();
            const description = card.querySelector('p').textContent.toLowerCase();
            
            if (title.includes(searchTerm) || description.includes(searchTerm)) {
                card.classList.remove('hidden');
            } else {
                card.classList.add('hidden');
            }
        });
    });
    
    // Filtrado por categoría
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Actualizar botones activos
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            const filter = this.getAttribute('data-filter');
            
            reportCards.forEach(card => {
                const category = card.getAttribute('data-category');
                
                if (filter === 'all' || filter === category) {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            });
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