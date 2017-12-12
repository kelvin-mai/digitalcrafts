let url = 'http://www.omdbapi.com/?apikey=thewdb',
    search;

$('#submit').click(function(e){
  e.preventDefault();
  search = $('#search').val();
  if (search){
    display(search);
  }
});

function display(search){
  $('#search-results').html('');
  $.get(`${url}&s=${search}`, function(data){
    if (data.Response === 'True'){
      data.Search.forEach(function(movie){
        $('#search-results').append($(`<li>${movie.Title}<button>Show</button></li>`).data('imdb',movie.imdbID));
      });
    } else {
      $('#search-results').html(`<h2>Error: ${data.Error}</h2>`);
    }
  });
}

$('#search-results').on('click','button',function(){
  let movie = $(this).parent().data('imdb');
  $.get(`${url}&i=${movie}`, function(data){
    $('#search-details').html(`
      <img src='${data.Poster}'></img>
      <div>
        <h3>${data.Title}</h3>
        <p><strong>Released</strong>: ${data.Released}</p>
        <p><strong>Rated</strong>: ${data.Rated}</p>
        <p><strong>Genre</strong>: ${data.Genre}</p>
        <p><strong>Director</strong>: ${data.Director}</p>
        <p><strong>Plot</strong>: ${data.Plot}</p>
      </div>
    `);
  });
});
