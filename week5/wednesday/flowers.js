$('button').click(function(e){
  e.preventDefault();
  $.post('https://flowers.vapor.cloud/flower', {
    name: $('#input-name').val(),
    description: $('#input-text').html(),
    imageURL: $('#input-img').val(),
  }, function(){
    $('#message').html('Successfully posted new flower!');
    populate();
  });
});

function populate(){
  $.get('https://flowers.vapor.cloud/flowers', function(data){
    data.forEach(function(flower){
      $('#flower-list').append(
        $(`
          <div class='flower-container'>
            <h3>${flower.name}</h3>
            <img src='${flower.imageURL}' alt='flower'/>
            <p>${flower.description}</p>
          </div>
        `)
      );
    });
  });
}

populate();
