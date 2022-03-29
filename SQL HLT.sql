show databases;

use headphones

create table headphone_details(
primary key (customers_ID),
vistors_ID varchar(3) not null,
wireless varchar(20)not null,
release_date date,
price decimal (9,2) not null,
model varchar not null
);
