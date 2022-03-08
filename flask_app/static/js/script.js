// Summernote
var allTextAreas = document.querySelectorAll('.summernote')
for (const element of allTextAreas) {
    $(element).summernote()
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

function formChange(el) {
    console.log(`logging el: ${el}`);
    updateElement(el)
    if (el.getAttribute('clear')) {
        el.value = ''
    }
    return el
}

function updateElement(el, form = null) {
    if (!form) {
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
    return el
}

// function showErrs(el, data) {
//     console.log(el);
// }


function setEventListeners(cls, eventType, func) {
    var allEvents = document.querySelectorAll(`.${cls}`)
    if (allEvents.length > 0) {
        for (const item of allEvents) {
            item.addEventListener(eventType, function () {
                func(item)
            })
        }
    }
}