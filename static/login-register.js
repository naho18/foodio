  "use strict";

  function logIn(evt) {

    $('#homepageForm').html(
        `<form action="/login" method="POST">
          <input name="email" type="text" class="form-control" placeholder="Email">
          <input name="password" type="password" class="form-control" placeholder="Password">
        <input type="submit" value="Log In">
        </form>
        `

      );
  }

  $('#login').click(logIn);


  function register(evt) {

    $('#homepageForm').html(
        `<form action="/registration" method="POST">
          <input name="name" type="text" class="form-control" placeholder="Name">
          <input name="email" type="text" class="form-control" placeholder="Email">
          <input name="password" type="password" class="form-control" placeholder="Password">
        <input type="Submit" value='Sign Up'>
        </form>
          `
      );

  }

  $('#register').click(register);
