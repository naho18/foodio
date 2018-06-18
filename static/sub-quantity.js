<!-- ////////////////////DECREASE QUANTITY OF FOOD////////////////////////// -->
"use strict";

function displayDecrease(results) {
    // refresh display food
    $('#display-food').load(" #display-food > *");
}


function subQuantity(param) {

    let food_id = document.querySelector(`p#${param.id}`);
    
    let formInputs = {
        "food-id": food_id.innerText,
    }

    $.get("/sub-quantity.json", 
           formInputs,
           displayDecrease);
}
