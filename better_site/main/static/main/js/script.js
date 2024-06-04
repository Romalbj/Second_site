const activePage = window.location.pathname;
//const Path = activePage.split("/");
//if(Path.includes("credit")|Path.includes("debit")|Path.includes("savings"))
//    {console.log('Hi')};
//console.log(Path);
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

//counters 2
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


//counters final
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
                    setTimeout(updateCount, 5);
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


const counters_2 = document.querySelectorAll('.counters_2 span');
const container_2 = document.querySelector('.counters_2');
let activated_2 = false;

window.addEventListener('scroll', () => {
    if(
            pageYOffset > container_2.offsetTop - container_2.offsetHeight - 400
            && activated_2 === false
    ) {
        counters_2.forEach(counter => {
            counter.innerText = 0;

            let count_2 = 0;

            function updateCount_2() {
                const target_2 = parseInt(counter.dataset.count);
                if(count_2 < target_2) {
                    count_2++;
                    counter.innerText = count_2;
                    setTimeout(updateCount_2, 5);
                } else {
                    counter.innerText = target_2;
                }
            }
            updateCount_2();
            activated_2 = true;
        });
    } else if(
        pageYOffset < container_2.offsetTop - container_2.offsetHeight - 500
        || pageYOffset === 0
        && activated_2 === true
 ) {
    counters_2.forEach(counter => {
            counter.innerText= 0;
    });
        activated_2 = false;
    }
});

const counters_3 = document.querySelectorAll('.counters_3 span');
const container_3 = document.querySelector('.counters_3');
let activated_3 = false;

window.addEventListener('scroll', () => {
    if(
            pageYOffset > container_3.offsetTop - container_3.offsetHeight - 400
            && activated_3 === false
    ) {
        counters_3.forEach(counter => {
            counter.innerText = 0;

            let count_3 = 0;

            function updateCount_3() {
                const target_3 = parseInt(counter.dataset.count);
                if(count_3 < target_3) {
                    count_3++;
                    counter.innerText = count_3;
                    setTimeout(updateCount_3, 5);
                } else {
                    counter.innerText = target_3;
                }
            }
            updateCount_3();
            activated_3 = true;
        });
    } else if(
        pageYOffset < container_3.offsetTop - container_3.offsetHeight - 500
        || pageYOffset === 0
        && activated_3 === true
 ) {
    counters_3.forEach(counter => {
            counter.innerText= 0;
    });
        activated_3 = false;
    }
});





function scrollHeader(){
    const header = document.getElementById('header')
    // When the scroll is greater than 80 viewport height, add the scroll-header class to the header tag
    if(this.scrollY >= 80) header.classList.add('scroll-header'); else header.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)


