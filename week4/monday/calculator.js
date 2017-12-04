// Create a calculator which allows the user to enter two numbers.
//
// * Calculator must consists of two textboxes for each input number.
//
// * Calculator must have 4 buttons for each operation "add, subtract, divide, multiply"
//
// * Calculator must have an equal to button "=" which when pressed shows the result
//
// * Calculator must display result in a nice, clear fashion to the user.
//
// * Calculator must have a "Clear" button to remove the inputs from the textboxes.
//
// * Calculator must clear the inputs when the user clicks "=" button.

let num1 = document.getElementById('num1'),
    num2 = document.getElementById('num2');

document.getElementById('calc-add').addEventListener('click', function(){
  document.getElementById('operator').innerHTML = '+';
});
document.getElementById('calc-subtract').addEventListener('click', function(){
  document.getElementById('operator').innerHTML = '-';
});
document.getElementById('calc-multiply').addEventListener('click', function(){
  document.getElementById('operator').innerHTML = '*';
});
document.getElementById('calc-divide').addEventListener('click', function(){
  document.getElementById('operator').innerHTML = '/';
});

document.getElementById('calc-equal').addEventListener('click', function(){
  let result = 0;
  if (document.getElementById('operator').innerHTML == '+') {
    result = parseInt(num1.value) + parseInt(num2.value);
  } else if (document.getElementById('operator').innerHTML == '-') {
    result = num1.value - num2.value;
  } else if (document.getElementById('operator').innerHTML == '*') {
    result = num1.value * num2.value;
  } else if (document.getElementById('operator').innerHTML == '/') {
    num2.value == 0 ? result = "Cannot divide by zero" : result = num1.value / num2.value;
  } else {
    result = 'ERROR!';
  }

  document.getElementById('resultant').innerHTML = result;
  clearNum();
});

function clearNum() {
  num1.value = '';
  num2.value = '';
}

document.getElementById('calc-clear').addEventListener('click', clearNum);
