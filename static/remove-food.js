 <!-- ///////////////////REMOVE ITEM TO REFRIGERATOR/////////////////////// -->
"use strict";

 function displayFood2(results) {
    // get display-food div by ID
    // remove item from list

    $("text").filter(":contains("+ results +")").remove()
    
    // reload/refresh div
    // $('#display-food').load(" #display-food > *");
    $("#remove-food").load(" #remove-food > *");


}

// jquery -- get values

function removeFood(evt) {
    evt.preventDefault();

    let formInputs = {
        "rm-ingredient": $("#rm-ingredient").val(),
    };
    console.log('remove food');
    console.log(formInputs);

// send to route

    $.post("/remove-food.json", 
           formInputs,
           displayFood2);
}

// event listener
$("#remove-food-form").on("submit", removeFood);