"use strict"; 

    function displayRecipes(results) {
        var recipes = results;

        let apiRecipes = []
        let i = 0

        for (let recipe of recipes) {
            // title
            apiRecipes.push("<div id='api-recipes' class='inline'>" + recipe['title'] + "<br>" + 
            
            // image with link to recipe
            `<a id=recipe${i} href="https://spoonacular.com/recipes/${recipe['title'].replace(
                / /g, '-')}-${recipe['id']}">` + "<br>" + 
            `<img id=recipe${i} src="${recipe['image']}" alt="Image"></a>` + "<br>" +
            
            // ingredient data
            `Num of Ingredients Used: ${recipe['usedIngredientCount']} ` + "<br>" +
            `Num of Ingredients Needed: ${recipe['missedIngredientCount']} ` + 
            
            // recipe title
            `<p hidden id=recipe${i} value="${recipe['title']}"> </p>` +

            // Add to favorites button
            `<button type='button' id=recipe${i} onClick="favRecipes(this)">&hearts;</button>`
            + "<br>" + "<br>" + "</div>");
            
            // increment i by 1
            i += 1

        }

        $('#recipediv').html(apiRecipes);
    }

// id=recipe${i}

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

        // refresh fav recipes 

        $('#display-favs').load(" #display-favs > *");
    }


    function refreshRecipes() {
        getRecipes();
        console.log("inside refresh recipes")

        // $('#display-recipes').load(" #display-recipes > *");
    }
