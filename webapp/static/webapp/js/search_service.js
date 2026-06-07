// Открыть/закрыть modal
const openFilterBtn = document.getElementById('openFilterBtn');
const closeFilterBtn = document.getElementById('closeFilterBtn');
const filterModal = document.getElementById('filterModal');

openFilterBtn.addEventListener('click', () => {
    filterModal.classList.add('active');
});

closeFilterBtn.addEventListener('click', () => {
    filterModal.classList.remove('active');
});

// Закрытие по Escape
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        filterModal.classList.remove('active');
    }
});

// Закрытие по клику вне контента
filterModal.addEventListener('click', (e) => {
    if (e.target === filterModal) {
        filterModal.classList.remove('active');
    }
});

// Поиск без перезагрузки (AJAX)
const searchBtn = document.getElementById('searchBtn');
const serviceInput = document.getElementById('service-input');
const zipInput = document.getElementById('zip-input');
const filterResults = document.getElementById('filterResults');

searchBtn.addEventListener('click', async () => {
    const service = serviceInput.value.trim();
    const zip = zipInput.value.trim();

    if (!service || !zip) {
        alert('Please enter both service and zip code');
        return;
    }

    // Показываем лоадер
    filterResults.innerHTML = '<p>Loading...</p>';

    try {
        const response = await fetch(`/api/find-pros/?service=${service}&zip=${zip}`);
        const data = await response.json();

        // Отображаем результаты
        if (data.pros.length === 0) {
            filterResults.innerHTML = '<p>No pros found</p>';
        } else {
            filterResults.innerHTML = data.pros.map(pro => `
        <div class="filter-pros-card">
          <h3>${pro.name}</h3>
          <p>${pro.service} - ${pro.zip}</p>
          <p>⭐ ${pro.rating} (${pro.reviews} reviews)</p>
          <button class="contact-btn">Contact</button>
        </div>
      `).join('');
        }
    } catch (error) {
        filterResults.innerHTML = '<p>Error loading results</p>';
    }
});
