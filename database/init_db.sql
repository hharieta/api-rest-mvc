-- from console do:
-- sqlite3 people.sqlite < init_db.sql
create table if not exists person(
    id integer not null primary key,
    lname varchar unique,
    fname varchar,
    timestamp datetime);

insert into person values 
    (1, "Fairy", "Tooth", "2022-10-08 09:15:10"),
    (2, "Ruprecht", "Knecht", "2022-10-08 09:15:13"),
    (3, "Bunny", "Easter", "2022-10-08 09:15:27");