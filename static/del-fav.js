<!-- ///////////////////////// DELETE FAV RECIPE ////////////////////////// -->
"use strict";

function refreshFavs(results) {
    // refresh display food
    $('#display-favs').load(" #display-favs > *");
}


function delRecipe(param) {

    let title = $(`button#${param.id}`).attr("value");

    let formInputs = {
        "title": title
    }

    $.get("/del-favs.json", 
           formInputs,
           refreshFavs);
}
