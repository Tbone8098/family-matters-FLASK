var allModalTriggers = document.querySelectorAll('.modal__trigger')
var allModalCloseBtns = document.querySelectorAll('.modal__close')
var allModalWrappers = document.querySelectorAll('.modal__wrapper')
var allModalContainers = document.querySelectorAll('.modal__container')

if (allModalTriggers.length > 0) {
    for (let btn of allModalTriggers) {
        btn.addEventListener('click', function () {
            let modalWrapper = document.querySelector(`[modal_name="${btn.getAttribute('modal_target')}"]`)
            console.log(modalWrapper);
            showModal(modalWrapper)
        })
    }

    for (let btn of allModalCloseBtns) {
        btn.addEventListener('click', function () {
            parent = findWrapper(btn)
            hideModal(parent)
        })
    }

    for (let wrapper of allModalWrappers) {
        wrapper.addEventListener('click', function(e){
            hideModal(wrapper)
        })
    }

    for (let container of allModalContainers) {
        container.addEventListener('click', function(e){
            e.stopPropagation()
        })
    }
}

function showModal(modal) {
    modal.classList.remove('d-none')
}

function hideModal(modal) {
    modal.classList.add("d-none")
}

function findWrapper(item) {
    parent = item.parentElement
    if (parent.classList.contains('modal__wrapper')) {
        return parent
    } else {
        return findWrapper(parent)
    }
}