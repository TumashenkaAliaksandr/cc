document.addEventListener('DOMContentLoaded', () => {

    const filterModal = document.getElementById('filterModal');
    const closeFilterBtn = document.getElementById('closeFilterBtn');

    if (!filterModal) {
        console.error('filterModal not found');
        return;
    }

    // Универсальное открытие модалки
    document.addEventListener('click', (e) => {

        const trigger = e.target.closest('.filter-open-trigger');

        if (!trigger) return;

        e.preventDefault();

        filterModal.classList.add('active');

    });

    // Закрытие крестиком
    closeFilterBtn?.addEventListener('click', () => {
        filterModal.classList.remove('active');
    });

    // Закрытие по Escape
    document.addEventListener('keydown', (e) => {

        if (e.key === 'Escape') {
            filterModal.classList.remove('active');
        }

    });

    // Закрытие по клику на фон
    filterModal.addEventListener('click', (e) => {

        if (e.target === filterModal) {
            filterModal.classList.remove('active');
        }

    });

});