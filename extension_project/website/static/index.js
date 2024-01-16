document.querySelector('#menu').addEventListener('click', ()=> {
    document.querySelector('nav ul').classList.toggle('showMenu');
})

const slider = document.querySelector('.slider');
const images = slider.querySelectorAll('img');
let currentIndex = 0;

    function showImage(index) {
        images.forEach((image, i) => {
        if (i === index) {
            image.style.display = 'block';
        } else {
            image.style.display = 'none';
        }
        });
    }

    function nextImage() {
        currentIndex++;
        if (currentIndex >= images.length) {
        currentIndex = 0;
        }
        showImage(currentIndex);
    }

    // Change image every 3 seconds (adjust as needed)
    setInterval(nextImage, 5000);

    // Show the initial image
    showImage(currentIndex);
