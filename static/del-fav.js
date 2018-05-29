<!-- ///////////////////////// DELETE FAV RECIPE ////////////////////////// -->
"use strict";

function refreshFavs(results) {
    // refresh display food
    $('#display-favs').load(" #display-favs > *");
    console.log('inside refreshFavs')
}


function delRecipe(param) {

    let title = $(`button#${param.id}`).attr("value");

    console.log(title)

    console.log("inside del recipe")

    let formInputs = {
        "title": title
    }

    console.log(formInputs);


// send to route

    $.get("/del-favs.json", 
           formInputs,
           refreshFavs);
}
