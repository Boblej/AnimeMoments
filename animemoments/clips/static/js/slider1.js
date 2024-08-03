var swiper = new Swiper(".mySwiper1", {
    direction: "horizontal",
    mousewheel: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    freeMode: true,
    loop: true,
    autoplay: {
        delay: 5000,
        disableOnInteraction: false,
        waitForTransition: true,
    },
    on: {
        init: function() {
            var swiperInstance = this;
            
            swiperInstance.el.addEventListener('mousedown', function() {
                swiperInstance.autoplay.stop();
            });
            
            swiperInstance.el.addEventListener('mouseup', function() {
                swiperInstance.autoplay.start();
            });
            
            swiperInstance.el.addEventListener('wheel', function() {
                swiperInstance.autoplay.stop();
            });

            swiperInstance.el.addEventListener('mouseleave', function() {
                swiperInstance.autoplay.start();
            });
        }
    },
    lazy: {
        loadPrevNext: true,
    }
});