let apiKey = '&apiKey=fdb094f592f94015af7480438307d05d',
  url = 'https://newsapi.org/v2/',
  sources = 'sources?language=en',
  headlines = 'top-headlines?';

let root = document.getElementById('root');

let populateSources = function() {
  root.innerHTML = '';
  axios.get(url + sources + apiKey)
  .then(function(res) {
    let json = JSON.parse(res.request.response);
    json.sources.forEach(function(source) {
      root.innerHTML += `
        <div>
          <h3>${source.name}</h3>
          <p>${source.description}</p>
          <button id='${source.id}'>Show Headlines</button>
        </div>
      `;
    });

    let buttons = document.getElementsByTagName('button');
    for (let i = 0; i<buttons.length; i++){
      buttons[i].addEventListener('click', function(){
        populateHeadlines(this.id);
      });
    }
    return res;
  }).catch(function(err) {
    console.log(err);
  });
}

populateSources();

let populateHeadlines = function(id){
  root.innerHTML = `<button onclick='populateSources()'>back</button>`;
  axios.get(url + headlines + 'sources=' + id + apiKey)
  .then(function(res){
    let json = JSON.parse(res.request.response);
    json.articles.forEach(function(article){
      root.innerHTML += `
        <div>
          <h3><a href='${article.url}'>${article.title}</a></h3>
          <h4>${article.author}</h4>
          <h4>${article.publishedAt}</h4>
          <img src=${article.urlToImage} alt=${article.title} />
          <p>${article.description}</p>
        </div>
      `;
    });
  }).catch(function(err){
    console.log(err);
  });
}
