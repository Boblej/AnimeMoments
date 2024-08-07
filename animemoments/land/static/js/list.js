const q = document.querySelectorAll('.faq-box');
const a = document.querySelectorAll('.faq-info');
const arrow = document.querySelectorAll('.arrow');

// цикл для анимации faq
for (let i = 0; i < q.length; i++) {
    q[i].addEventListener('click', function () {

        a[i].classList.toggle('faq-info-opened')

        arrow[i].classList.toggle('arrow-rotated')
    })
 
}