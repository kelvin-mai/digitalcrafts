let root = document.getElementById('root');

let populate = function(){
fetch('https://flowers.vapor.cloud/flowers')
  .then(function(response){ return response.json(); })
  .then(function(json){
     json.forEach(function(flower){
       root.innerHTML += `
         <h3>${flower.name}</h3>
         <img src=${flower.imageURL} />
         <p>${flower.description}</p>
       `;
     });
   });
}

document.getElementById('input-submit').addEventListener('click', function(e){
  e.preventDefault();
  let name =  document.getElementById('input-name').value,
    description =  document.getElementById('input-description').value,
    imageURL =  document.getElementById('input-image').value;
  if (name && description && imageURL){
    fetch('https://flowers.vapor.cloud/flower', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name,
        description,
        imageURL
      })
    }).then(function(response) {
      return response.json();
    }).then(function(data){
      populate();
    });
  }
});


populate();
