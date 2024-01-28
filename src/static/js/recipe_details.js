document.addEventListener(
    'DOMContentLoaded', async () => {

        const recipeID = getRecipeID()
        let ingredientID = null


        // Load recipe data
        const recipe_data = await APICall(`/recipe/${recipeID}`, "GET")
        processRecipeInfo(recipe_data)

        // Load ingredients data
        const ingredient_data = await APICall(`/ingredients/${recipeID}`, "GET")
        processRecipeIngredients(ingredient_data)

        // Insert current title and preparation to the edit modal
        document.querySelector("#recipe-title-edit").addEventListener(
            'click', () => {
                document.querySelector("#input-name").value = document.querySelector("#recipe-title").innerText
                document.querySelector("#input-preparation").value = document.querySelector("#recipe-preparation").innerText
            }
        )

        // Handle recipe name/preparation edit
        document.querySelector("#recipe-edit-form").addEventListener(
            'submit', async () => {
                const response = await APICall(`/recipe/${recipeID}`, "PUT",
                    {
                        "name": document.querySelector("#input-name").value,
                        "preparation": document.querySelector("#input-preparation").value
                    }
                )
                if (response["message"] !== "Success") {
                    alert(response["message"])
                }
                location.reload()
            })

        // Handle recipe deletion
        document.querySelector('#recipe-delete').addEventListener('click', (e) => {
            const confirmModal = new bootstrap.Modal('#confirmationModal', {
                keyboard: false
            })
            confirmModal._element.querySelector('#confirmDelete').addEventListener(
                'click', async () => {
                    await APICall(`/recipe/${recipeID}`, "DELETE")
                    window.location.href = '/'
                })
            confirmModal.show()
        })

        // Handle adding new ingredient
        document.querySelector("#new-ingredient-form").addEventListener(
            'submit', async () => {
                const response = await APICall(`/ingredients/${recipeID}`, "POST",
                    {
                        "name": document.querySelector("#input-ingredient-name").value,
                        "quantity": document.querySelector("#input-ingredient-quantity").value,
                        "unit": document.querySelector("#input-ingredient-unit").value
                    }
                )
                if (response["message"] !== "Success") {
                    alert(response["message"])
                }
            })

        // Remove ingredient
        document.querySelector("#confirmationModal").addEventListener("show.bs.modal", function (event) {
            var button = event.relatedTarget
            ingredientID = button.getAttribute("data-id")
        })

        document.querySelector("#confirmDelete").addEventListener(
            'click', async () => {
                const response = await APICall(`/ingredient/${ingredientID}`, "DELETE")
                if (response["message"] !== "Success") {
                    alert(response["message"])
                }
                location.reload()
            })
    })



// Processing functions 

function getRecipeID() {
    const subURL = window.location.pathname
    return parseInt(subURL.split('/')[2])
}


function processRecipeInfo(data) {
    const editedElement = document.querySelector('#recipe-title')
    const preparationText = document.querySelector('#recipe-preparation')

    editedElement.innerText = data['name']
    const replaced_prep = data['preparation'] ? data['preparation'].replaceAll(/\d+\./g, "</br>$&") : null
    preparationText.innerHTML = replaced_prep
}


function processRecipeIngredients(ingredients) {
    const recipeIngredients = document.querySelector("#recipe-ingredients")
    for (let ingredientNumber in ingredients) {
        if (ingredients.hasOwnProperty(ingredientNumber)) {
            const ingredient_data = ingredients[ingredientNumber]
            const section = document.createElement('li')
            section.className = 'mt-2'
            section.innerHTML = `
            <div class='row'>
                <div class="col">
                    <p class="d-inline">${ingredient_data['Ingredient.name']}</p>
                </div>
                <div class="col">
                    <p>${ingredient_data['RecipeIngredient.quantity']}${ingredient_data['RecipeIngredient.unit']}</p>
                </div>
                <div class="col-5">
                    <button 
                        data-id=${ingredient_data['RecipeIngredient.id']} 
                        class="btn btn-light btn-sm recipe-ingredient-delete" 
                        data-bs-toggle="modal" 
                        data-bs-target="#confirmationModal">
                            Delete
                    </button>
                </div>
            </div>
            `
            recipeIngredients.appendChild(section)
        }
    }
}


async function removeIngredient(url) {
    const response_data = await APICall(url, 'DELETE')
    alert(response_data)
}

// No sleep, keed the screen on 
var noSleep = new NoSleep();
var wakeLockEnabled = false;
var toggleEl = document.querySelector("#toggle");
toggleEl.addEventListener('click', function () {
    if (!wakeLockEnabled) {
        noSleep.enable(); // keep the screen on!
        wakeLockEnabled = true;
        toggleEl.value = "Disable wake lock";
        toggleEl.style.background = '#66BB55';
    } else {
        noSleep.disable(); // let the screen turn off.
        wakeLockEnabled = false;
        toggleEl.value = "Enable wake lock";
        toggleEl.style.background = ''
    }
}, false);
