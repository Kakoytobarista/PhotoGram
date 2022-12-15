import {autocompleteDiv, peopleOnPhotoField} from "./constants.js";
import {getAutocompletePeopleName} from "./requests.js";

let arrayAutocompleteValues = []

function setAttributes(el, attrs) {
    for (let key in attrs) {
        el.setAttribute(key, attrs[key]);
    }
}

export async function createElementsAutocomplete() {
    const divWithElements = document.getElementById('myInputautocomplete-list')
    console.log(divWithElements == null)
    window.peoples = getAutocompletePeopleName().then((data) => {
    return data
})
    if (divWithElements != null) {
        divWithElements.remove()
    }
    setAttributes(autocompleteDiv.appendChild(document.createElement("div")),
        {
            'id': 'myInputautocomplete-list',
            'class': 'autocomplete-items'
        }
    )


    arrayAutocompleteValues.length = 0
    for (let i = 0; i < await window.peoples.then((data) => {
        return data.length}); i++) {
        arrayAutocompleteValues.push(await window.peoples.then((data) => {
            return data[i]
        }))

        if (arrayAutocompleteValues[i].includes(peopleOnPhotoField.value)) {
            let divAutocompleteVar = document.querySelector(
                '.autocomplete-items').appendChild(document.createElement('div'))

            // divAutocompleteVar.textContent = arrayAutocompleteValues[i].slice(peopleOnPhotoField.value.length, -1)

            let inputAutocompleteVar = divAutocompleteVar.appendChild(document.createElement('input'))
            console.log(inputAutocompleteVar)
            inputAutocompleteVar.value = String(arrayAutocompleteValues[i])
            inputAutocompleteVar.readonly = true
            inputAutocompleteVar.type = 'hide'


        }
    }

    console.log(arrayAutocompleteValues)
    let matches = arrayAutocompleteValues.filter(s => s.includes(peopleOnPhotoField.value));

}

