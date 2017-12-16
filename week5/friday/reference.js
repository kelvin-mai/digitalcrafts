 config = {
  apiKey: "AIzaSyDbqltBBdJG6d9-rVve4MftAAohGUwpZR4",
  authDomain: "grocery-app-2d723.firebaseapp.com",
  databaseURL: "https://grocery-app-2d723.firebaseio.com",
  projectId: "grocery-app-2d723",
  storageBucket: "",
  messagingSenderId: "397856840472"
};
firebase.initializeApp(config);

let database = firebase.database().ref(),
    root = document.getElementById('root'),
    list = document.getElementById('list');

document.getElementById('button').addEventListener('click', function(){
  let val = document.getElementById('input');
  database.push().set({
    val: val.value
  });
  val.value = ''
});

database.on('value', snapshot => {
  list.innerHTML = '';
  for (key in snapshot.val()){
    list.innerHTML += `
      <li>
        ${snapshot.val()[key].val}
        <button
          id='${key}'
          class='grocery-btn'>Click Me</button>
      </li>
      `;
    let buttons = document.getElementsByClassName('grocery-btn');
    for (let i=0;i<buttons.length;i++){
      buttons[i].addEventListener('click', function(){ console.log(this.id) });
    }
  }
});
