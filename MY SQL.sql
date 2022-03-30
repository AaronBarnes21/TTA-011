show databases;

use headset;

create table headsets_details(
primary key(reg_id),
reg_id  int not null,
wireless varchar(20)not null,
delivery_date date,
price decimal (6,2)not null,
model varchar (20),
make varchar (20) not null);

insert into headsets_details (reg_id, wireless, delivery_date, model, make)
values('1','yes','01042022','14','PS5','Turtle beach'),
('2','yes','30042022','180','Xbox Series','ASTRRO'),
('3','no','04042022','43','Nintendo switch','SteelSeries'),
('4','no','10042022','45','PC','Logitech G43'),
('5','yes','09042022','PS4','Logictech G435'),
('6','yes','01042022','Mac','Logictech G935'),
('7','no','02042022','74','Xbox One','HP Omen'),
('9','no','29032022','19','PC','USB Headset'),
('10','no','01042022','21.49','PS5','Soulbytes');
explain headset_details;
select * from headset_details;

delete from headset_details
where reg_id = '1';
select * from headset_details;

insert into headset_details
values('6','yes','01042022','Mac','Logictech G935');


select * from headset_details;

select price, delivery_date from  headset_details;


select * from headset_details
where customers_ID = '3';

select * from headset_details order by reg_id;

select * from headset_details order by price;

select * from orders
where price between 14 and 180;

select delivery_date,wirless from headset_details order by wireless, delivery_date;





