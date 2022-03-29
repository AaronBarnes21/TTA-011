show databases;

use headset;

create table headset_details(
primary key (reg_id),
reg_id  int not null,
wireless varchar(20)not null,
delivery_date date,
price decimal (9,2) not null,
model varchar (20),
make varchar (10) not null);

