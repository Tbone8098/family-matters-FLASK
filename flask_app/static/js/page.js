var menuItems = document.querySelectorAll('.menu-item')

for (const btn of menuItems) {
    btn.addEventListener('click', function () {
        let type = this.getAttribute('type')
        if (type == 'content'){
            let url = this.getAttribute('url')
            let form = new FormData()
            form.append('page_id', btn.getAttribute('page_id'))

            fetch(url, {
                method: 'post',
                body: form
            })
            .then(resp => resp.json())
            .then(data => {
                let blockArea = document.querySelector('.block_area')
                let textarea = document.createElement('textarea')
                textarea.setAttribute('name', 'content')
                textarea.setAttribute('id', 'content')
                textarea.setAttribute('url', `/api/block/content/${data['data']['id']}/update`)
                textarea.setAttribute('cols', 30)
                textarea.setAttribute('rows', 10)
                textarea.textContent = "Insert Text Here"
                textarea.addEventListener('change', function(){
                    updateElement(this)
                })
                
                let divContainer = document.createElement('div')
                divContainer.classList.add('m-3')
                
                divContainer.append(textarea)
                blockArea.append(divContainer)
            })
            
        } else if (type == 'images'){
            // console.log('images');
        }
    })
}

function updatePage(data) {
    let tableBody = document.querySelector('#page_table_body')
    tableBody.innerHTML += `
    <tr>
        <td>${data['name']}</td>
        <td>${data['author']}</td>
        <td>now</td>
        <td>
            <a class="m-0 btn bg__pine" href="/page/${data['id']}/edit">Edit</a>
            <a class="m-0 btn btn-danger" href="/page/${data['id']}/delete">Delete</a>
        </td>
    </tr>
    `
}