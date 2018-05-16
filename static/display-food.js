<!-- ////////////////////DISPLAY FOOD TO HOMEPAGE ///////////////////////// -->
"use strict";

    function setData(results) {
        var dataset = results;
        console.log(dataset);
        alert("it works");
    }

    function getData() {
        $.get('/food-data.json', setData);
    }

    getData();
