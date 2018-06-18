 <!-- ///////////////////REMOVE ITEM TO REFRIGERATOR/////////////////////// -->
"use strict";

 function displayFood2(results) {    
    // reload/refresh div
    $("#rmfood").load(" #rmfood > *");
    $('#display-food').load(" #display-food > *");

}

function removeFood(evt) {
    evt.preventDefault();

    let formInputs = {
        "rm-ingredient": $("#rm-ingredient").val(),
    };

    $.post("/remove-food.json", 
           formInputs,
           displayFood2);
}

$("#remove-food-form").on("submit", removeFood);