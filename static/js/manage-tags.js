const ENTER_KEY_CODE = 13

let tags = []
let words_typed = ''
let input_tags = document.getElementById("tags-input")
let list_tags = document.getElementById("list-tags")
let tags_values_to_backend = document.getElementById("tags")

function add_tag(event) {
    if((event.type === 'keydown'  && ENTER_KEY_CODE === event.keyCode) || event.type === 'blur') {

        if (!tags.includes(words_typed) && words_typed !== '') {
            
            tags.push(words_typed)
            show_tag(words_typed)

            tags_values_to_backend.value = tags
            input_tags.value = ''
            words_typed = ''
        } else
            input_tags.value = ''

    }
}

function input_action(event) {

    let value = event.target.value.toLowerCase()

    if ((value.length === 1 && value !== '') || words_typed.length >= 1) {
        
        words_typed = value

    } else if (!tags.includes(value) && value !== ''){

        tags.push(value)
        show_tag(value)
        tags_values_to_backend.value = tags
        input_tags.value = ''

    } else
        input_tags.value = ''
    
}

function show_tag(tag) {

    let element_list = document.createElement("li")
    element_list.innerHTML = tag
    element_list.dataset.option = tag
    element_list.addEventListener('mousedown', removeElement)

    let x_field  = document.createElement('span')
    x_field.innerHTML = 'x'

    element_list.appendChild(x_field)
    element_list.classList.add('tag-list__element')

    list_tags.appendChild(element_list)
    
}


function removeElement(event) {

    if (event.target.nodeName === 'SPAN'){
        tags = tags.filter(value => value !== event.target.parentNode.dataset.option)
        event.target.parentNode.remove()

    } else {
        tags = tags.filter(value => value !== event.target.dataset.option)
        event.target.remove()
    }

    tags_values_to_backend.value = tags

}


input_tags.addEventListener('input', input_action)
input_tags.addEventListener('blur', add_tag )
input_tags.addEventListener('keydown', add_tag )
