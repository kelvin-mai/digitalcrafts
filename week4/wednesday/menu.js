let desserts = [],
    entrees = [],
    starters = [];

function display(dish){
  let menuItem = $('<div/>').appendTo($('#menu')).addClass('menu-item');
  $('<h2/>').appendTo(menuItem).text(dish['title']);
  $('<img/>').appendTo(menuItem).attr('src',dish['imageURL']);
  $('<p/>').appendTo(menuItem).text(dish['description']);
  $('<p/>').appendTo(menuItem).text('$' + dish['price']);
};

function init(){
  dishes.forEach(function(dish){
    display(dish);
  });
}

function setArr(){
  dishes.forEach(function(dish){
    if (dish['course'] == 'Starters'){
      starters.push(dish);
    } else if (dish['course'] == 'Entrees'){
      entrees.push(dish);
    } else if (dish['course'] == 'Desserts'){
      desserts.push(dish);
    }
  });
}

function sortedDisplay(course){
  $('.menu-item').remove();
  if (course == 'starters'){
    starters.forEach(function(dish){ display(dish) });
  } else if (course == 'entrees'){
    entrees.forEach(function(dish){ display(dish) });
  } else if (course == 'desserts'){
    desserts.forEach(function(dish){ display(dish) });
  } else {
    init();
  }
}

$('button').each(function(){
  $(this).click(function(){
    $('button').removeClass('is-active');
    $(this).addClass('is-active');
    sortedDisplay($(this).text().toLowerCase());
  });
});


init();
setArr();
