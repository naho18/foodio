 <!-- ///////////////////REMOVE ITEM TO REFRIGERATOR/////////////////////// -->

 function displayFood2(results) {
    // get display-food div by ID
    // remove item from list

    // $("p").filter(":contains('{}')".format(results)).remove();
    $("p").filter(":contains("+ results +")").remove()
    // $("p").filter(":contains(' Hello ')").remove()
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