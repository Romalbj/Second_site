const activePage = window.location.pathname;
console.log(activePage);
const navLinks = document.querySelectorAll('.nav_link');
console.log(navLinks);
forEach(link => {
    if(link.href.includes(`${activePage}`))
        link.classList.add('active');

})


function scrollHeader(){
    const header = document.getElementById('header')
    // When the scroll is greater than 80 viewport height, add the scroll-header class to the header tag
    if(this.scrollY >= 80) header.classList.add('scroll-header'); else header.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)


