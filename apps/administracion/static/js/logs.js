const searchInput = document.getElementById('searchInput');
const filterUsuario = document.getElementById('filterUsuario');
const filterAccion = document.getElementById('filterAccion');
const resetBtn = document.getElementById('resetFilters');
const rows = document.querySelectorAll('#logsTable tr');

function filterLogs() {
    const search = searchInput.value.toLowerCase();
    const usuario = filterUsuario.value.toLowerCase();
    const accion = filterAccion.value.toLowerCase();

    rows.forEach(row => {
        const rowUsuario = row.cells[1].textContent.toLowerCase();
        const rowAccion = row.cells[2].textContent.toLowerCase();

        if (
            (rowUsuario.includes(search) || rowAccion.includes(search)) &&
            (usuario === "" || rowUsuario === usuario) &&
            (accion === "" || rowAccion === accion)
        ) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}

// Eventos
searchInput.addEventListener('keyup', filterLogs);
filterUsuario.addEventListener('change', filterLogs);
filterAccion.addEventListener('change', filterLogs);
resetBtn.addEventListener('click', () => {
    searchInput.value = '';
    filterUsuario.value = '';
    filterAccion.value = '';
    filterLogs();
});