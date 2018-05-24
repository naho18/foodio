"use strict"; 

    function displayRecipes(results) {
        var recipes = results;

        var list = ["<h2>Recipes</h2>"]

        let i = 0

        for (let recipe of recipes) {
            // title
            list.push("<div id='recipediv'>" + recipe['title'] + "<br>" + 
            // image with link to recipe
            `<a id=recipe${i} href="https://spoonacular.com/recipes/${recipe['title'].replace(
                / /g, '-')}-${recipes[0]['id']}">` + "<br>" + 
            `<img src="${recipe['image']}" alt="Image"></a>` + "<br>" +
            // ingredient data
            `Num of Ingredients Used: ${recipe['usedIngredientCount']} ` + "<br>" +
            `Num of Ingredients Needed: ${recipe['missedIngredientCount']} ` + 
            
            // `<p hidden id=recipe${i}>
            //   spoonacular.com/recipes/${recipe['title'].replace(/ /g, '-')}-${recipes[0]['id']}
            // </p>`


            // button
            `<button type='button' id=recipe${i} onClick="favRecipes(this)">&hearts;</button>`
            + "<br>" + "<br>" + "</div>");
            i += 1

        }

        $('#display-recipes').html(list);
    }

// id=recipe${i}

    function getRecipes() {
        $.get('/recipes.json', displayRecipes);
    }

    getRecipes();


    function favRecipes(param) {

        let link = $(`a#${param.id}`).attr("href");
        let img = $('img').attr("src");

        console.log(link)
        console.log(img)
        console.log("inside fav-recipes")

        let formInputs = {
            "fav-url": link,
            "img" : img
        }

        console.log(formInputs);

    // send to route
        $.get("/fav-recipes.json", 
               formInputs,
               displayFavs);
    }

    function displayFavs(results) {
        // refresh display food
        console.log("inside displayFavs")

        // $('#display-food').load(" #display-food > *");
    }
