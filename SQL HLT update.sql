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

insert into headset_details(reg_id,wirless,delivery_date,price,model,make)
values('1','yes','01042022','14','PS5','Turtle beach recon'),
('2','yes','30042022','180','Xbox Series','ASTRRO'),
('3','no','04042022','43','Nintendo switch','SteelSeries'),
('4','no','10042022','45','PC','Logitech G43'),
('5','yes','09042022','PS4','Logictech G435'),
('6','yes','01042022','Mac','Logictech G935'),
('7','no','02042022','74','Xbox One','HP Omen Blast'),
('9','no','29032022','19','PC','USB Headset'),
('10','no','01042022','21.49','PS5','Soulbytes');


select * from headset_details;

delete from headset_details
where reg_id = '1';
select * from headset_details;

insert into headset_details
values('10','no','01042022','21.49','PS5','Soulbytes');


select * from headset_details;

select price, delivery_date from  headset_details;


select * from headset_details
where customers_ID = '6';

select * from headset_details order by price;

select * from headset_details order by reg_id;

select delivery_date,wirless from headset_details order by wireless, delivery_date

select * from headset_details where price between  10 and 200;

