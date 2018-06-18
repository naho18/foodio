
<!-- ////////////////////ADD ITEM TO REFRIGERATOR////////////////////////// -->
"use strict";

function displayFood(results) {
    // refresh add & remove foods div
    $('#display-food').load(" #display-food > *");
    $("#rmfood").load(" #rmfood > *");
    $("#addfood").load(" #addfood > *");

}

function addFood(evt) {
    evt.preventDefault();
    let formInputs = {
        "ingredient": $("#ingredient").val(),
        "quantity": $("#quantity").val(),
    };

    $.post("/add-food.json", 
           formInputs,
           displayFood);
}

$("#add-food-form").on("submit", addFood);
