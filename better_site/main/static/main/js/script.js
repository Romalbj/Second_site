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


//Horizontal sctoll text
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


let valueDisplays = document.querySelectorAll(".num");
let interval = 5000;

console.log(valueDisplays);

valueDisplays.forEach((valueDisplay) => {
    let startValue = 0;
    let endValue = parseInt(valueDisplay.getAttribute("data-val"));
    console.log(endValue);
    let duration = Math.floor(interval / endValue);
    let counter = setInterval(function () {
        startValue += 1;
        valueDisplay.textContent = startValue;
        if(startValue == endValue) {
            clearInterval(counter);
        }
    }, duration);
});



const counters = document.querySelectorAll('.counters span');
const container = document.querySelector('.counters');
let activated = false;

window.addEventListener('scroll', () => {
    if(
            pageYOffset > container.offsetTop - container.offsetHeight - 400
            && activated === false
    ) {
        counters.forEach(counter => {
            counter.innerText = 0;

            let count = 0;

            function updateCount() {
                const target = parseInt(counter.dataset.count);
                if(count < target) {
                    count++;
                    counter.innerText = count;
                    setTimeout(updateCount, 10);
                } else {
                    counter.innerText = target;
                }
            }
            updateCount();
            activated = true;
        });
    } else if(
        pageYOffset < container.offsetTop - container.offsetHeight - 500
        || pageYOffset === 0
        && activated === true
 ) {
    counters.forEach(counter => {
            counter.innerText= 0;
    });
        activated = false;
    }
});







function scrollHeader(){
    const header = document.getElementById('header')
    // When the scroll is greater than 80 viewport height, add the scroll-header class to the header tag
    if(this.scrollY >= 80) header.classList.add('scroll-header'); else header.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)


