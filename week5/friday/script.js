let config = {
  apiKey: "AIzaSyDbqltBBdJG6d9-rVve4MftAAohGUwpZR4",
  authDomain: "grocery-app-2d723.firebaseapp.com",
  databaseURL: "https://grocery-app-2d723.firebaseio.com",
  projectId: "grocery-app-2d723",
  storageBucket: "",
  messagingSenderId: "397856840472"
};
firebase.initializeApp(config);

let db = firebase.database().ref(),
    root = $('#root'),
    data = [];

db.on('value', snap => {
  data = [];
  for (key in snap.val()){
    data.push({
      key,
      category: snap.val()[key].category,
      items: snap.val()[key].items || null
    });
  }
  display();
});

let display = () => {
  root.html('');
  data.forEach(card => {
    root.append($(`
      <h3>${card.category}</h3>
      <form id='${card.key}'>
        <input placeholder='Add grocery item'/>
        <button>Submit</button>
      </form>
    `).on('submit', addItem));
    if (card.items){
      card.items.forEach(item => root.append(`<li>${item}</li>`));
    }
  });
}

$('#category-form').on('submit', e => {
  e.preventDefault();
  db.push().set({
    category: $('#category-form input').val(),
    items: []
  });
});

let removeCard = function(e) {
  e.preventDefault();
  let id = `${$(this).attr('id')}`;
  db.child(id).remove();
}

let addItem = function(e) {
  e.preventDefault();
  let id = `${$(this).attr('id')}`,
      obj = data.find((i) => i.key === id),
      added = $(`#${id} input`).val();
  obj.items ? obj.items.push(added) : obj.items = [added];
  db.child(id).update(obj);
}
