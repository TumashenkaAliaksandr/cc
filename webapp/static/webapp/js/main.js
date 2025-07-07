document.addEventListener('DOMContentLoaded', () => {
    const mainPhotoLink = document.querySelector('.photo-gallery > a'); // ссылка вокруг главного фото
    const mainPhoto = document.getElementById('mainPhoto');
    const thumbsContainer = document.querySelector('.additional-photos');
    const thumbs = document.querySelectorAll('.additional-photos .thumb');

    // Функция для получения массива всех изображений (главное + миниатюры)
    function getAllImages() {
        const srcs = [mainPhoto.src];
        thumbs.forEach(thumb => {
            if (!srcs.includes(thumb.src)) srcs.push(thumb.src);
        });
        return srcs;
    }

    // При клике на миниатюру меняем главное фото и меняем миниатюру на бывшее главное фото
    thumbs.forEach(thumb => {
        thumb.style.cursor = 'pointer';
        thumb.addEventListener('click', () => {
            // Сохраняем текущие данные главного фото
            const oldSrc = mainPhoto.src;
            const oldAlt = mainPhoto.alt;

            // Меняем главное фото на выбранную миниатюру
            mainPhoto.src = thumb.src;
            mainPhoto.alt = thumb.alt;

            // Меняем миниатюру на бывшее главное фото
            thumb.src = oldSrc;
            thumb.alt = oldAlt;

            // Обновляем href у ссылки вокруг главного фото, чтобы лайтбокс открывал правильное изображение
            mainPhotoLink.href = mainPhoto.src;
        });
    });

    // Обработчик клика по главному фото — открываем лайтбокс
    mainPhotoLink.addEventListener('click', (e) => {
        e.preventDefault();

        const images = getAllImages();
        let currentIndex = images.indexOf(mainPhoto.src);

        let onKeyDownHandler;

        const instance = basicLightbox.create(`
            <div class="lightbox-container" style="
                position: relative;
                max-width: 90vw;
                max-height: 90vh;
                margin: auto;
                border-radius: 10px;
                overflow: hidden;
                background: #000;
                display: flex;
                align-items: center;
                justify-content: center;
            ">
                <button id="closeBtn" style="
                    position: absolute;
                    top: 10px;
                    right: 10px;
                    background: transparent;
                    border: none;
                    font-size: 2rem;
                    color: white;
                    cursor: pointer;
                    z-index: 10;
                    user-select: none;
                " aria-label="Close">&times;</button>
                <button id="prevBtn" style="
                    position: absolute;
                    top: 50%;
                    left: 10px;
                    transform: translateY(-50%);
                    font-size: 2rem;
                    background: transparent;
                    border: none;
                    color: white;
                    cursor: pointer;
                    user-select: none;
                    z-index: 10;
                " aria-label="Previous">&#10094;</button>
                <img src="${images[currentIndex]}" style="
                    max-width: 100%;
                    max-height: 100%;
                    border-radius: 10px;
                    user-select: none;
                " alt="Gallery image" />
                <button id="nextBtn" style="
                    position: absolute;
                    top: 50%;
                    right: 10px;
                    transform: translateY(-50%);
                    font-size: 2rem;
                    background: transparent;
                    border: none;
                    color: white;
                    cursor: pointer;
                    user-select: none;
                    z-index: 10;
                " aria-label="Next">&#10095;</button>
            </div>
        `, {
            onShow: (instance) => {
                const closeBtn = instance.element().querySelector('#closeBtn');
                const prevBtn = instance.element().querySelector('#prevBtn');
                const nextBtn = instance.element().querySelector('#nextBtn');
                const img = instance.element().querySelector('img');

                closeBtn.onclick = () => instance.close();

                prevBtn.onclick = () => {
                    currentIndex = (currentIndex - 1 + images.length) % images.length;
                    img.src = images[currentIndex];
                };

                nextBtn.onclick = () => {
                    currentIndex = (currentIndex + 1) % images.length;
                    img.src = images[currentIndex];
                };

                instance.element().addEventListener('click', e => {
                    if (e.target === instance.element()) {
                        instance.close();
                    }
                });

                onKeyDownHandler = (e) => {
                    if (e.key === 'ArrowLeft') prevBtn.click();
                    else if (e.key === 'ArrowRight') nextBtn.click();
                    else if (e.key === 'Escape') instance.close();
                };

                document.addEventListener('keydown', onKeyDownHandler);
            },
            onClose: () => {
                document.removeEventListener('keydown', onKeyDownHandler);
            }
        });

        instance.show();
    });
});
