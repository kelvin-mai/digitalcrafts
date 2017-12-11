let pendingTasks = [], completedTasks = [];
if (localStorage.pendingTasks){
  pendingTasks = JSON.parse(localStorage.pendingTasks);
}
if (localStorage.completedTasks){
  completedTasks = JSON.parse(localStorage.completedTasks);
}

pendingTasks.forEach(function(task){
  addPending(task);
});
completedTasks.forEach(function(task){
  addCompleted(task);
});

$('#task-add').click(function(event){
  event.preventDefault();
  let task = $('#task-input').val();
  if (task){
    $('#task-input').val('');
    addPending(task);
  }
});

$('#pending, #completed').sortable().on('click', 'span', function(){
  $(this).parent().remove();
});

$('#pending').on('change', 'input', function(){
  $(this).parent().remove();
  $('#completed').append($(this).parent());
});

$('#completed').on('change', 'input', function(){
  $(this).parent().remove();
  $('#pending').append($(this).parent());
});

function addPending(task){
  $('#pending').append(
    $('<li/>').text(task).append($('<span class="task-remove">Remove</span>'))
      .prepend($('<input type=checkbox />'))
  );
}

function addCompleted(task){
  $('#completed').append(
    $('<li/>').text(task).append($('<span class="task-remove">Remove</span>'))
      .prepend($('<input type=checkbox />'))
  );
}
