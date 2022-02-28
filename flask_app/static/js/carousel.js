var prevBtn = document.querySelector('#prev')
var nextBtn = document.querySelector('#next')

prevBtn.addEventListener('click', function(){
    console.log('prev');
    nextSlide(-1)
})
nextBtn.addEventListener('click', function(){
    console.log('next');
    nextSlide(1)
})

function nextSlide(direction){
    var activeCarousel = document.querySelector('.carousel__container.active')
    if (direction > 0){
        let next = activeCarousel.nextElementSibling
        if (!next){
            activeCarousel.parentElement.firstElementChild.classList.add('active')
        }else {
            next.classList.add('active')
        }
    } else if (direction < 0){
        let prev = activeCarousel.previousElementSibling
        if (!prev){
            activeCarousel.parentElement.lastElementChild.classList.add('active')
        } else {
            prev.classList.add('active')
        }
    }

    activeCarousel.classList.remove('active')
    
}