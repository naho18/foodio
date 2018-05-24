<!-- ///////////////////////////FAVORITE RECIPES ////////////////////////// -->
"use strict";

function displayFavs(results) {
    // refresh display food
    console.log("inside displayFavs")

    // $('#display-food').load(" #display-food > *");
}


function favRecipes(param) {

    let url = document.querySelector(`a#${param.id}`);

    console.log(url.innerText)

    console.log("inside fav-recipes")

    let formInputs = {
        "fav-url": url.innerText,
    }

    console.log(formInputs);


// send to route

    $.get("/fav-recipes.json", 
           formInputs,
           displayFavs);
}

export {favRecipes};