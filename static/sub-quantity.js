<!-- ////////////////////DECREASE QUANTITY OF FOOD////////////////////////// -->
"use strict";

function displayDecrease(results) {
    // refresh display food
    $('#display-food').load(" #display-food > *");
}


function subQuantity(param) {

    let food_id = document.querySelector(`p#${param.id}`);

    console.log(food_id.innerText)
    console.log("inside subQuantity")
    
    let formInputs = {
        "food-id": food_id.innerText,
    }

    console.log(formInputs);


// send to route

    $.get("/sub-quantity.json", 
           formInputs,
           displayDecrease);
}
