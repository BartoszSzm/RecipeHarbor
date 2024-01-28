document.addEventListener('DOMContentLoaded', async () => {
    const response_data = await APICall('/recipies', 'GET')
    processRecipiesList(response_data)
})


function processRecipiesList(data) {
    const container = document.getElementById('recipies-area')
    for (const row of data) {
        const card = createRecipecard(
            id = row['Recipe.id'],
            meal_type = row['Recipe.meal_type'],
            name = row['Recipe.name'],
            category_name = row['Category.name']
        )
        container.appendChild(card)
    }
    // After successfull loading of all cards, run live search
    loadLiveSearch()

    function createRecipecard(id, meal_type, name, category_name) {
        // Create element filled with given recipe info 
        const newCard = document.createElement('div')
        newCard.className = 'col recipe-element'
        newCard.innerHTML = `
    <div class='card border-dark mb-3 h-100 card-style' style='18rem'>
        <div id='card-header' class="card-header bg-transparent">${meal_type}</div>
        <div class="card-body" style="--bs-card-title-spacer-y:-1rem">
            <h5 id='card-title' class="card-title">${name}</h5>
        </div>
            <div id='card-footer' class="card-footer bg-transparent">${category_name}</div>
    </div>
    `;
        // Attach event listener
        newCard.addEventListener('click', () => {
            window.location.href = `/recipedetails/${id}`
        })
        return newCard
    }
}

function loadLiveSearch() {
    // Prepare constants
    const recipiesArea = document.getElementById('recipies-area')
    const searchBar = document.querySelector('#search-bar input')
    const allRecipies = recipiesArea.querySelectorAll('.recipe-element')

    // Listen for input letters in searchBar, place divs if recipe name match input phrases
    searchBar.addEventListener('input', () => {
        const inputText = searchBar.value.toLowerCase()

        allRecipies.forEach((recipe) => {
            recipeName = recipe.querySelector('#card-title').innerText.toLowerCase()

            if (recipeName.includes(inputText)) {
                recipe.style.display = 'block'
            } else {
                recipe.style.display = 'none'
            }
        })
    })
}

// Add new recipe
document.addEventListener('DOMContentLoaded', () => {
    addRecipeSubmit = document.querySelector('#add-new-recipe-button')
    addRecipeSubmit.addEventListener('click', async () => {
        const data = {
            "name": document.querySelector("#input-new-recipe-name").value,
            "meal_type": document.querySelector("#input-new-recipe-meal-type").value,
        }
        await APICall(`/recipies`, "POST", data)
        location.reload()
    })
})