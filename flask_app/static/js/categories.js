function updatePage(data) {
    let tableBody = document.querySelector('#category_table_body')
    console.log(data);
    tableBody.innerHTML += `
    <tr>
        <td>${data['name']}</td>
        <td>
            <a class="m-0 btn bg__pine" href="/category/${data['id']}/edit">Edit</a>
            <a class="m-0 btn btn-danger" href="/category/${data['id']}/delete">Delete</a>
        </td>
    </tr>
    `
}