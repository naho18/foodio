<!-- ////////////////////INCREASE QUANTITY OF FOOD////////////////////////// -->
"use strict";

function displayIncrease(results) {
    // refresh display food
    $('#display-food').load(" #display-food > *");
}


function addQuantity(param) {

    let food_id = document.querySelector(`p#${param.id}`);

    console.log(food_id.innerText)

    console.log("inside add quantity")

    let formInputs = {
        "food-id": food_id.innerText,
    }

    console.log(formInputs);


// send to route

    $.get("/add-quantity.json", 
           formInputs,
           displayIncrease);
}
