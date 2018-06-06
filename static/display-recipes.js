 // has class vs removeClass


"use strict"; 

    function displayRecipes(results) {
        var recipes = results;

        let apiRecipes = []
        let i = 0

        for (let recipe of recipes) {
            // title
            apiRecipes.push("<div id='api-recipes' class='inline'>" +
            `<h5><a id=recipe${i} href="https://spoonacular.com/recipes/${recipe['title'].replace(
                / /g, '-')}-${recipe['id']}">${recipe['title']} </a>` +
            `<img id=recipe${i} src="${recipe['image']}" alt="image">` +
            `<text class="recipetext">Ingredients Used: ${recipe['usedIngredientCount']}, Needed: ${recipe['missedIngredientCount']}     </text>` + 
            `<p hidden id=recipe${i} value="${recipe['title']}"> </p>` +
            `<button type='button' class='inline' id=recipe${i} onClick="favRecipes(this)">&hearts;</button>`
             + "<br>" + "<br>" + "</div>");

            
            // increment i by 1
            i += 1

        }

        $('#recipediv').html(apiRecipes);
    }


    function getRecipes() {
        $.get('/recipes.json', displayRecipes);
    }

    getRecipes();


    function favRecipes(param) {

        let link = $(`a#${param.id}`).attr("href");
        let img = $(`img#${param.id}`).attr("src");
        let title = $(`p#${param.id}`).attr("value");

        console.log(title)
        console.log(link)
        console.log(img)


        $(`button#${param.id}`).attr('style', 'background-color:red; color:white; padding: 0.25em 1em; border-radius: 20px;');


        console.log("inside fav-recipes")

        let formInputs = {
            "fav-url": link,
            "img" : img,
            "title" : title
        }

        console.log(formInputs);

    // send to route
        $.get("/fav-recipes.json", 
               formInputs,
               displayFavs);
    }

    function displayFavs() {
        $('#display-favs').load(" #display-favs > *");
    }


    function refreshRecipes() {
        getRecipes();
        $('#display-recipes').load(" #display-recipes > *");
    }
