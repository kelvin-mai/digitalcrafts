let url='http://dc-coffeerun.herokuapp.com/api/coffeeorders/';

$('#place-order').click(function(e){
  e.preventDefault();
  let p = $('.message').val('');
  let emailAddress = $('#input-email').val(),
      coffee = $('#input-coffee').val();
  $.ajax({
    type: 'POST',
    url,
    data: {
      emailAddress,
      coffee
    },
    success: function(data){
      $(p).html(`You just ordered a ${data.coffee}`).addClass('success').removeClass('error');
      $('#coffee-list').html('');
      getCoffee();
    },
    error: function(err){
      $(p).html(err.message).addClass('error').removeClass('success');
    }
  });
});

$('#lookup-order').click(function(e){
  e.preventDefault();
  let p = $('.message').val('');
  let emailAddress = $('#lookup-email').val();
  $.ajax({
    url: url+emailAddress,
    success: function(data){
      $(p).html(`
        <h1>email: ${data.emailAddress}</h1>
        <p>Coffee: ${data.coffee}</p>
        `).addClass('success').removeClass('error');
    },
    error: function(err){
      $(p).html(err.message).addClass('error').removeClass('success');
    }
  });
});

$('#delete-order').click(function(e){
  e.preventDefault();
  let p = $('.message').val('');
  let emailAddress = $('#lookup-email').val();
  $.ajax({
    type: 'DELETE',
    url: url+emailAddress,
    success: function(data){
      $(p).html(`${emailAddress} has been removed`).removeClass('success').addClass('error');
      $('#coffee-list').html('');
      getCoffee();
    },
    error: function(err){
      $(p).html(err.message).addClass('error').removeClass('success');
    }
  });
});

function getCoffee(){
  $.ajax({
    url,
    success: function(data){
      for(const prop in data){
        $('#coffee-list').append(
          $(`
            <div>
              <h3>email Address: ${data[prop].emailAddress}</h3>
              <p>Coffee: ${data[prop].coffee}</p>
            </div>
          `)
        );
      }
    }
  });
}

getCoffee();
