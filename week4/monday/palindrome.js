// Create a webpage which will ask the user for an input and determines whether that input was palindrome or not.


document.getElementById('palindrome-btn').addEventListener('click', function(){
  str = document.getElementById('palindrome-input').value;
  if (str.toLowerCase() == str.toLowerCase().split('').reverse().join('')) {
    document.getElementById('is-palindrome').innerHTML = "That's a palindrome!";
    console.log(true);
  } else {
    document.getElementById('is-palindrome').innerHTML = "That's not a palindrome!";
    console.log(false);
  }
});
