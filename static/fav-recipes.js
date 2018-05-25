<!-- ///////////////////////////FAVORITE RECIPES ////////////////////////// -->
"use strict";


export function favRecipes(param) {

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
    };



    function displayFavs(results) {
        // refresh display food
        console.log("inside displayFavs")

// export {favRecipes};