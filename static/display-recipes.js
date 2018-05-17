"use strict";

    
    function displayRecipes(results) {
        var recipes = results;

        var list = []

        for (let recipe of recipes) {
            list.push("<div id='recipediv'>" + recipe['title'] 
            + "<br>" + 

            `<a id='img'href="https://spoonacular.com/recipes/${recipe['title'].replace(
                / /g, '-')}-${recipes[0]['id']}">` 

            + "<br>" + 
            `<img src="${recipe['image']}" alt="Image">` + "</a>" 

            + "<br>" +
            `Num of Ingredients Used: ${recipe['usedIngredientCount']} ` 

            + "<br>" +

            `Num of Ingredients Needed: ${recipe['missedIngredientCount']} ` 
            + "<br>" + "<br>" + "<br>" + "</div>");
        }
        console.log(list)
        console.log(results)


        $('#display-recipes').html(list);
    }

    function getRecipes() {
        $.get('/recipes.json', displayRecipes);
    }

    getRecipes();
