function updatePage(data) {
    if (data['type'] === 'addrow'){
        let tableBody = document.querySelector('#category_table_body')
        console.log(data);
        tableBody.innerHTML += `
        <tr id="${data['id']}">
        <td>${data['name']}</td>
        <td>
        <span class="m-0 btn bg__pine edit__btn" category_id="${data['id']}">Edit</span>
        <a class="m-0 btn btn-danger" href="/category/${data['id']}/delete">Delete</a>
        </td>
        </tr>
        `
        setEventListeners('edit__btn', 'click', editOnClick)
    }
    else if (data['type'] === 'update cell'){
        let row = document.getElementById(data['id'])
        let td = row.firstElementChild
        console.log(td);
        let content = td.firstElementChild.value
        td.innerHTML = content
    }
}

setEventListeners('edit__btn', 'click', editOnClick)

function editOnClick(btn){
    let editSection = btn.parentElement.parentElement.children[0]
    let editSectionText = editSection.textContent
    let id = btn.getAttribute('category_id')
    editSection.innerHTML = `<input class="onChangeEl" type="text" name="name" id="name" value="${editSectionText}" url="/api/category/${id}/update">`
    x = setEventListeners('onChangeEl', 'change', formChange)
}