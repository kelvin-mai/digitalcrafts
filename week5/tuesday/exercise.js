$.get('https://jsonplaceholder.typicode.com/users', function(data){
  data.forEach(function(user){
    $('#root').append(
      $(`
        <li>
          <p>Name: ${user.name}</p>
          <p>Username: ${user.username}</p>
          <p>email: ${user.email}</p>
          <p>Address: ${user.address.street} ${user.address.suite}</p>
          <p>${user.address.city} ${user.address.zipcode}</p>
          <p>Phone: ${user.phone}</p>
          <p>Wobsite: ${user.website}</p>
          <p>Company: ${user.company.name}</p>
          <p>${user.company.catchPhrase}
          <p>${user.company.bs}</p>
        </li>
      `)
    );
  });
});
