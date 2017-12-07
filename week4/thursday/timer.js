let intervalId,
  timerValue,
  timerDisplay = document.getElementById('timer-display');

document.getElementById('timer-btn').addEventListener('click', function() {
  timerValue = document.getElementById('timer-input').value;

  if (timerValue <= 0) {
    timerDisplay.innerText = 'Please enter a positive value!';
    clearInterval(intervalId);
    return;
  }

  timerDisplay.innerText = timerValue;

  intervalId = window.setInterval(function() {
    timerValue -= 1;
    timerDisplay.innerText = timerValue;
    if (timerValue < 1)
      clearInterval(intervalId);
    }
  , 1000);

});
