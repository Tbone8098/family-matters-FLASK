var onChangeEl = document.querySelectorAll('.onChangeEl')

if (onChangeEl.length > 0) {
    for (const el of onChangeEl) {
        el.addEventListener('change', function () {
            updateElement(this)
            if (this.getAttribute('clear')) {
                this.value = ''
            }
        })
    }
}

function updateElement(el) {
    let form = new FormData()
    form.append(el.id, el.value)
    let url = el.getAttribute('url')

    fetch(url, {
        method: 'post',
        body: form
    })
        .then(resp => resp.json())
        .then(data => {
            if (data.status == 500) {
                showErrs(el, data)
            } else if (data.status == 200) {
                updatePage(data['data'])
            }
        })
}

function showErrs(el, data) {
    console.log(el);
}