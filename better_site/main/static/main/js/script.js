const activePage = window.location.pathname;
console.log(activePage);
const navLinks = document.querySelectorAll('.nav_link');
console.log(navLinks);
navLinks.forEach (link => {
    if(link.href.includes(`${activePage}`))
        link.classList.add('active');
})

const width = window.innerWidth;
const height = window.innerHeight;

console.log("Ширина экрана: " + width + "px");
console.log("Высота экрана: " + height + "px");



let scrollContainer = document.querySelector('.rec_list');
let arrow_backward = document.getElementById('arrow_backward');
let arrow_forward = document.getElementById('arrow_forward');

scrollContainer.addEventListener('wheel', (evt) => {
    evt.preventDefault();
    scrollContainer.scrollLeft += evt.deltaY;
    scrollContainer.style.scrollBehavior = 'auto';

});

arrow_forward.addEventListener('click', () => {
    scrollContainer.style.scrollBehavior = 'smooth';
    scrollContainer.scrollLeft += 500;
});

arrow_backward.addEventListener('click', () => {
    scrollContainer.style.scrollBehavior = 'smooth';
    scrollContainer.scrollLeft -= 500;
});



function scrollHeader(){
    const header = document.getElementById('header')
    // When the scroll is greater than 80 viewport height, add the scroll-header class to the header tag
    if(this.scrollY >= 80) header.classList.add('scroll-header'); else header.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)


