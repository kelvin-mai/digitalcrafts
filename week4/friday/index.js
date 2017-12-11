function myMap() {
  var mapProp = {
    center: new google.maps.LatLng(51.508742, -0.120850),
    zoom: 5
  };
  var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

let container = document.getElementById('container');

users.forEach(function(user) {
  let template = `
    <div class='contact'>
      <div class='contact-info'>
        <p>Name: ${user.name}</p>
        <p>User Name: ${user.username}</p>
        <p>Email: ${user.email}</p>
        <p>Address: ${user.address.street}
        ${user.address.suite}</p><p>
        ${user.address.city}
        ${user.address.zipcode}</p>
      </div><div class='contact-business'>
        <button onclick='updateMap(${user.address.geo.lat}, ${user.address.geo.lng})'>Geolocation </button>
        <p>Phone: ${user.phone}</p>
        <p>Website: ${user.website}</p>
        <p>Company: ${user.company.name}</p>
      </div>
    </div>
  `

  container.innerHTML += template;
});

function updateMap(lat, lng) {
  var mapProp = {
    center: new google.maps.LatLng(lat, lng),
    zoom: 5
  };
  var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}
