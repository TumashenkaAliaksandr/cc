document.addEventListener('DOMContentLoaded', () => {
    const mainPhoto = document.getElementById('mainPhoto');
    const thumbs = document.querySelectorAll('.additional-photos .thumb');

    // Массив всех фото (основное + доп.)
    const images = [
        mainPhoto.src,
        ...Array.from(thumbs).map(img => img.src)
    ];

    // При клике на доп. фото меняем основное
    thumbs.forEach((thumb, index) => {
        thumb.style.cursor = 'pointer';
        thumb.addEventListener('click', () => {
            mainPhoto.src = thumb.src;
            mainPhoto.alt = thumb.alt;
        });
    });

    // При клике на основное фото открываем lightbox с возможностью листать все фото
    mainPhoto.addEventListener('click', () => {
        let currentIndex = images.indexOf(mainPhoto.src);

        const instance = basicLightbox.create(`
        <div class="lightbox-container" style="position:relative; text-align:center;">
          <img src="${images[currentIndex]}" style="max-width:90vw; max-height:90vh; border-radius:10px;" />
          <button id="prevBtn" style="position:absolute; top:50%; left:10px; transform:translateY(-50%); font-size:2rem; background:none; border:none; color:white; cursor:pointer;">&#10094;</button>
          <button id="nextBtn" style="position:absolute; top:50%; right:10px; transform:translateY(-50%); font-size:2rem; background:none; border:none; color:white; cursor:pointer;">&#10095;</button>
        </div>
      `, {
            onShow: (instance) => {
                const prevBtn = instance.element().querySelector('#prevBtn');
                const nextBtn = instance.element().querySelector('#nextBtn');
                const img = instance.element().querySelector('img');

                prevBtn.onclick = () => {
                    currentIndex = (currentIndex - 1 + images.length) % images.length;
                    img.src = images[currentIndex];
                };
                nextBtn.onclick = () => {
                    currentIndex = (currentIndex + 1) % images.length;
                    img.src = images[currentIndex];
                };
            }
        });

        instance.show();
    });
});
