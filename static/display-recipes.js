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
                / /g, '-')}-${recipe['id']}">` + "<br>" + 
            `<img id=recipe${i} src="${recipe['image']}" alt="Image"></a>` + "<br>" +
            
            // ingredient data
            `Num of Ingredients Used: ${recipe['usedIngredientCount']} ` + "<br>" +
            `Num of Ingredients Needed: ${recipe['missedIngredientCount']} ` + 
            
            // recipe title
            `<p hidden id=recipe${i} value="${recipe['title']}"> </p>` +

            // button
            `<button type='button' id=recipe${i} onClick="favRecipes(this)">&hearts;</button>`
            + "<br>" + "<br>" + "</div>");
            
            // increment i by 1
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

    function displayFavs(results) {
        var favlist = ["<h2>Favorite Recipes</h2>"];

        console.log(results);

        // loop over results to display recipe
        for (let recipe of results) {
            // title
            list.push(`<div id='favrecipes'>recipe[0] <br>
            <a href="${recipe[1]}"><br>
            <img src"${recipe[2]}" alt="Image"></a><br><br>
            `)

        }

        console.log(results)

        $('#display-favs').html(favlist);

        // $('#display-food').load(" #display-food > *");
    }
