create table students (
  studentid serial primary key,
  firstname varchar(50),
  lastname varchar(50),
  graduated boolean not null default 'f',
  cohort integer not null
);

select * from students;
insert into students (firstname, lastname, graduated, cohort) values ('john', 'doe', 't', 2018);
insert into students (firstname, lastname, cohort) values ('mary','jane',2017);
insert into students (firstname, lastname, graduated, cohort) values ('alex', 'lowe', 't', 2015);
select studentid, firstname where cohort = 2018;
update students set cohort = 2018 where studentid = 1;
delete from students where studentid = 1;

create table projects (
  projectid serial primary key,
  name varchar(200) not null,
  studentid integer references students(studentid)
);

insert into projects(name, studentid) values('My Web App', 3);
insert into projects(name, studentid) values('iPhone App', 3);
insert into projects(name, studentid) values('Android App Using React', 2);

select students.studentid, firstname, lastname, name from students join projects on students.studentid = projects.studentid;

select count(studentid) from students;
select sum(studentid) from students;
select cohort, count(cohort) from students group by cohort;
select firstname, lastname, count(projectid) from students join projects on students.studentid = projects.studentid group by students.studentid;

drop table projects;
