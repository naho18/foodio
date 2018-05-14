// event listener, AJAX request


function displayFood(results) {
    console.log(results);
    $('#ingredient').html(results);
}

// jquery to get values


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

$("#add-food-form").on("submit", addFood);



// route returns json (fish)

// add to end of food-display div