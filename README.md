### Table Schema

```:sqlite3
CREATE TABLE Log(
id integer primary key autoincrement,
status text not null,
person integer not null,
date_time text default current_timestamp
);

CREATE TABLE Member(
id integer not null primary key,
name text not null
);
```
