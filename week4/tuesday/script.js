let username = document.getElementById('username'),
    password = document.getElementById('password'),
    login = document.getElementById('login'),
    remember = document.getElementById('remember'),
    display = document.getElementById('display');

login.addEventListener('click', function(){
  if (remember.checked == true){
    alert('Credentials are saved.');
  } else {
    alert('No one will remember you!');
  }

  display.innerHTML = username.value + ':' + password.value;
});
