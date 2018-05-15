
<!-- ////////////////////ADD ITEM TO REFRIGERATOR////////////////////////// -->

function displayFood(results) {
    // get display-food div by ID
    // append to end of loop
    $('#display-food').append(results);
}

// jquery -- get values

function addFood(evt) {
    evt.preventDefault();

    let formInputs = {
        "ingredient": $("#ingredient").val(),
        "quantity": $("#quantity").val(),
        "food_type": $("#food_type").val(),
    };
    console.log('add food');
    console.log(formInputs);

// send to route

    $.post("/add-food.json", 
           formInputs,
           displayFood);
}

// event listener
$("#add-food-form").on("submit", addFood);
