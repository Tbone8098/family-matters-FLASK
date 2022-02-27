// Summernote
var allTextAreas = document.querySelectorAll('.summernote')
for (const element of allTextAreas) {
    $(element).summernote()
    console.log(typeof element);
}

// summernote save
var summernoteForms = document.querySelectorAll('.summernote-form')
for (const formEl of summernoteForms) {
    formEl.addEventListener('submit', function (e) {
        e.preventDefault()
        form = new FormData(formEl)
        updateElement(formEl, form)
    })
}

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

function updateElement(el, form = null) {
    if (!form){
        form = new FormData()
        form.append(el.id, el.value)
    }
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