var newsResetBtn = document.querySelector('#news_reset_btn')

newsResetBtn.addEventListener('click', function(){
    this.parentElement.parentElement.children[2].children[2].children[2].textContent = ""
    this.parentElement.parentElement.children[1].textContent = ""
})
