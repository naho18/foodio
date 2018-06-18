<!-- ////////////////////INCREASE QUANTITY OF FOOD////////////////////////// -->
"use strict";

function displayIncrease(results) {
    // refresh display food
    $('#display-food').load(" #display-food > *");
}


function addQuantity(param) {

    let food_id = document.querySelector(`p#${param.id}`);
    let formInputs = {
        "food-id": food_id.innerText,
    }

    $.get("/add-quantity.json", 
           formInputs,
           displayIncrease);
}
