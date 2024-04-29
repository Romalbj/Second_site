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


function scrollHeader(){
    const header = document.getElementById('header')
    // When the scroll is greater than 80 viewport height, add the scroll-header class to the header tag
    if(this.scrollY >= 80) header.classList.add('scroll-header'); else header.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)


