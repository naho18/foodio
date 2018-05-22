
<!-- ////////////////////ADD ITEM TO REFRIGERATOR////////////////////////// -->
"use strict";

function displayFood(results) {
    // get display-food div by ID
    // append to end of loop
    // $('#display-food').append(results);

    // refresh add & remove foods div
    console.log(results)
    console.log("inside display food")

    $('#display-food').load(" #display-food > *");
    $("#rmfood").load(" #rmfood > *");
}

// jquery -- get values

function addFood(evt) {
    evt.preventDefault();
    console.log("inside add food")

    let formInputs = {
        "ingredient": $("#ingredient").val(),
        "quantity": $("#quantity").val(),
        "food_type": $("#food_type").val(),
    };

// send to route

    $.post("/add-food.json", 
           formInputs,
           displayFood);
}

// event listener
$("#add-food-form").on("submit", addFood);
