
var allCategoryPickerBtn = document.querySelectorAll('.category_picker')

for (const btn of allCategoryPickerBtn) {
    btn.addEventListener('click', function () {
        removeActive()
        btn.classList.add('active')
        let categoryId = btn.getAttribute('category_id')
        fetch(`/api/category/${categoryId}`)
            .then(resp => resp.json())
            .then(data => {
                console.log(data);
                let container = document.querySelector('#post-container')
                console.log(container);
                container.innerHTML = ''
                for (let i = 0; i < 4; i++){
                    post = data['content'][i]
                    container.innerHTML += `
                    <div class="border shadow p-3 d-flex flex-column justify-content-center post__container">
                        <h1 class="text-center mt-auto">${post['name']}</h1>
                        <img class="mt-auto" src="${post['cover_picture']}" alt="" width="200px">
                        <a class="btn bg__charcoal txt__sunglow mt-auto" href="/post/${post['id']}">View More</a>
                    </div>
                `
                }
            })
    })
}

function removeActive(){
    for (const btn of allCategoryPickerBtn) {
        btn.classList.remove('active')
    }
}