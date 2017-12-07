let newsSection = document.getElementById('news');

news.articles.forEach(function(article){
  let author = article.author,
      title = article.title,
      description = article.description,
      url = article.url,
      imageUrl = article.urlToImage,
      published = article.publishedAt;

  newsSection.innerHTML += `
    <div class='Article'>
      <h2><a href='${url}'>${title}</a></h2>
      <h3>${author}</h3>
      <img src='${imageUrl}'></img>
      <p class='Article-description'>${description}</p>
      <p class='Article-published'><em>${published}</em></p>
    </div>
  `;
});
