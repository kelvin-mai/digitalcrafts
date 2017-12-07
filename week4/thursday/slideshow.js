slideshow = document.getElementById('slideshow');

images = [
  'https://images.unsplash.com/photo-1488190211105-8b0e65b80b4e?auto=format&fit=crop&w=1950&q=80&ixid=dW5zcGxhc2guY29tOzs7Ozs%3D',
  'https://images.unsplash.com/photo-1485069203392-8e1aeb1ebf02?auto=format&fit=crop&w=1954&q=80&ixid=dW5zcGxhc2guY29tOzs7Ozs%3D',
  'https://images.unsplash.com/photo-1509957660513-3cfee07defec?auto=format&fit=crop&w=1987&q=80&ixid=dW5zcGxhc2guY29tOzs7Ozs%3D',
  'https://images.unsplash.com/photo-1488485300416-de7f8f876d4b?auto=format&fit=crop&w=1950&q=80&ixid=dW5zcGxhc2guY29tOzs7Ozs%3D',
  'https://images.unsplash.com/photo-1489684141651-7e45b4e77b3a?auto=format&fit=crop&w=1917&q=80&ixid=dW5zcGxhc2guY29tOzs7Ozs%3D',
  'https://images.unsplash.com/photo-1483383490964-8335c18b6666?auto=format&fit=crop&w=1867&q=80&ixid=dW5zcGxhc2guY29tOzs7Ozs%3D',
  'https://images.unsplash.com/reserve/NnDHkyxLTFe7d5UZv9Bk_louvre.jpg?auto=format&fit=crop&w=1940&q=80&ixid=dW5zcGxhc2guY29tOzs7Ozs%3D'
];

let count = 0;
window.setInterval(function(){
  slideshow.innerHTML = `<img style='width: 100%' src='${images[count]}' />`
  count++;
  if (count >= images.length) count = 0;
},1000);
