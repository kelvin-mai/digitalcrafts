\connect kelvinmai;
drop database shoppingdb;
create database shoppingdb;
\connect shoppingdb;

create table shoppinglists (
  id serial not null unique primary key,
  name varchar(50) not null
);

create table groceryitems (
  id serial not null unique primary key,
  name varchar(50),
  shoppinglistid integer references shoppinglists(id),
  quantity integer default 0,
  price decimal default 0.0
);

insert into shoppinglists (name) values
  ('Walmart'), ('HEB'), ('Whole Foods');

insert into groceryitems (shoppinglistid, name, quantity, price) values
  (1, 'Pepper', 2, 1),
  (1, 'Salt',1,1),
  (1, 'Milk',1,5),
  (1, 'Bread',1,4),
  (1, 'Sour cream',1,2),
  (2,'Mustard',1,1),
  (2,'Ketchup',1,2),
  (2,'Orange Juice',1,5),
  (2,'Onion',1,3),
  (2,'Jalapenos',1,5),
  (3, 'Bananas', 1, 3),
  (3, 'Almond Butter', 1, 2),
  (3, 'Cold Brew Coffee', 1, 10),
  (3, 'Vegan Cheese', 1, 8),
  (3, 'Vegan Sasauge', 1, 12);

select * from shoppinglists;
select * from groceryitems;
select * from groceryitems where price >= 10;
select max(price) as maxprice from groceryitems;
select min(price) as minprice from groceryitems;
select sum(price) as sum from groceryitems;

select shoppinglists.id, shoppinglists.name, groceryitems.name, quantity, price from shoppinglists join groceryitems on shoppinglists.id = 1;
select shoppinglists.name, count(shoppinglists.id) as items from groceryitems join shoppinglists on shoppinglists.id = groceryitems.shoppinglistid group by shoppinglists.name;
select shoppinglists.name, sum(groceryitems.shoppinglistid) as items from groceryitems join shoppinglists on shoppinglists.id = groceryitems.shoppinglistid group by shoppinglists.name;

insert into groceryitems (shoppinglistid, name, quantity, price) values (1, 'Pepper', 3, 2);
select * from groceryitems where name = 'Pepper';
insert into groceryitems (shoppinglistid, name, quantity, price) values (3, 'Vegan Butter', 1, 10);
insert into groceryitems (shoppinglistid, name, quantity, price) values (3, 'French Press', 1, 20);
select * from groceryitems where price >= 10 and price <= 15;
