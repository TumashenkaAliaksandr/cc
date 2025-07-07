document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.getElementById('orderFormToggle');
    const content = document.getElementById('orderFormContent');

    toggle.addEventListener('click', () => {
        const isHidden = content.classList.toggle('hidden');
        toggle.textContent = isHidden ? 'Click to order Service ▼' : 'Click to order Service ▲';
        toggle.setAttribute('aria-expanded', !isHidden);
    });

    // Также можно добавить открытие/закрытие по клавише Enter или Space для доступности
    toggle.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            toggle.click();
        }
    });
});
