// слайдер на главной странице
const swiper = new Swiper('.swiper', {
    autoplay: {
        delay: 5000,
        disableOnInteraction: false,
    },
    direction: 'horizontal',
    loop: true,
    mousewheel: true,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    scrollbar: {
        el: '.swiper-scrollbar',
        draggable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    speed: 800,
    freeMode: true,
});
