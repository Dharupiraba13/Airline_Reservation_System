
/* Insert into Charges Table */
insert into charges values (1, 'Cancellation fee (2-24 hours)',3500);
insert into charges values (2, 'Cancellation fee (24 hours and above)',3000);
insert into charges values (3, 'Cancellation fee (Before 72 hours of departure)',0);
insert into charges values (4, 'Cancellation fee (2-24 hours)',3750);
insert into charges values (5, 'Cancellation fee (2-24 hours)',3250);
insert into charges values (6, 'Cancellation fee (24 hours and above)',3250);
insert into charges values (7, 'Cancellation fee (24 hours and above)',3000);
insert into charges values (8, 'No-show fee',6000);
insert into charges values (9, 'No-show fee',4000);
insert into charges values (10, 'No-show fee',6500);
insert into charges values (11, 'No-show fee',4500);
insert into charges values (12, 'No-show fee',5000);
insert into charges values (13, 'Changes fee (2-24 hours)',3250);
insert into charges values (14, 'Changes fee (24 hours and above)',2750);
insert into charges values (15, 'Changes fee (2-24 hours)',2750);
insert into charges values (16, 'Changes fee (24 hours and above)',2500);
insert into charges values (17, 'Changes fee (2-24 hours)',3000);
insert into charges values (18, 'Extra Baggage',900);
insert into charges values (19, 'Extra Baggage',1800);
insert into charges values (20, 'Taxes',12);
insert into charges values (21, 'Taxes',5);

/* Insert into Aircrafts Table */
insert into Aircrafts (Aircraft_id,Capacity,Company) values ('A320_CEO',180,'InterGlobe Aviation Limited');
insert into Aircrafts (Aircraft_id,Capacity,Company) values ('A320_NEO',186,'InterGlobe Aviation Limited');
insert into Aircrafts (Aircraft_id,Capacity,Company) values ('A321',232,'InterGlobe Aviation Limited');
insert into Aircrafts (Aircraft_id,Capacity,Company) values ('ATR',78,'InterGlobe Aviation Limited');
insert into Aircrafts (Aircraft_id,Capacity,Company) values ('Boeing 737-700_Layout1',149,'Spicejet Limited');
insert into Aircrafts (Aircraft_id,Capacity,Company) values ('Boeing 737-700_Layout2',134,'Spicejet Limited');
insert into Aircrafts (Aircraft_id,Capacity,Company) values ('Boeing 737-800',189,'Spicejet Limited');
insert into Aircrafts (Aircraft_id,Capacity,Company) values ('Boeing 737-900ER',212,'Spicejet Limited');
insert into Aircrafts (Aircraft_id,Capacity,Company) values ('Boeing 787',256,'TATA Groups');
insert into Aircrafts (Aircraft_id,Capacity,Company) values ('A320-214_CEO',180,'Conglomerate Wadia Group');
insert into Aircrafts (Aircraft_id,Capacity,Company) values ('A320-271_NEO',186,'Conglomerate Wadia Group');
insert into Aircrafts (Aircraft_id,Capacity,Company) values ('A321_CEO',158,'TATA Sons');
insert into Aircrafts (Aircraft_id,Capacity,Company) values ('A321_NEO',158,'TATA Sons');
insert into Aircrafts (Aircraft_id,Capacity,Company) values ('Boeing 737-800NG',168,'TATA Sons');
insert into Aircrafts (Aircraft_id,Capacity,Company) values ('Boeing 787-9 Dreamliner',299,'TATA Sons');
insert into Aircrafts (Aircraft_id,Capacity,Company) values ('A330-200-254_PAX',254,'Naresh Goyal');
insert into Aircrafts (Aircraft_id,Capacity,Company) values ('ATR-72-600-72_PAX',72,'Naresh Goyal');
insert into Aircrafts (Aircraft_id,Capacity,Company) values ('ATR-72-500-72_PAX',72,'Naresh Goyal');
insert into Aircrafts (Aircraft_id,Capacity,Company) values ('B737-700-134_PAX',134,'Naresh Goyal');
insert into Aircrafts (Aircraft_id,Capacity,Company) values ('B737-900-166_PAX',166,'Naresh Goyal');
insert into Aircrafts (Aircraft_id,Capacity,Company) values ('B737-900ER-184_PAX',184,'Naresh Goyal');


/* Insert into Passengers Table */
insert into Passengers (Passenger_id,Name,Email,Phone_number,Type) values (101,'Raj','raj03@gmail.com',9443012345,'adult');
insert into Passengers (Passenger_id,Name,Email,Phone_number,Type) values (102,'Geetha','geetha13@gmail.com',9443009876,'adult');
insert into Passengers (Passenger_id,Name,Email,Phone_number,Type) values (103,'Anil','anil93@gmail.com',94896014593,'adult');
insert into Passengers (Passenger_id,Name,Email,Phone_number,Type) values (104,'Surya','surya007@gmail.com',7513600765,'adult');
insert into Passengers (Passenger_id,Name,Email,Phone_number,Type) values (105,'Kumar','kumar45@gmail.com',9443078901,'adult');
insert into Passengers (Passenger_id,Name,Email,Phone_number,Type) values (106,'Nakul','nakul78@gmail.com',9489612789,'adult');
insert into Passengers (Passenger_id,Name,Email,Phone_number,Type) values (107,'Cathy','cathy12@gmail.com',9451285679,'adult');
insert into Passengers (Passenger_id,Name,Email,Phone_number,Type) values (108,'Henry','henry89@gmail.com',7590147890,'adult');
insert into Passengers (Passenger_id,Name,Email,Phone_number,Type) values (109,'Sharma','sharma001@gmail.com',9409012667,'adult');
insert into Passengers (Passenger_id,Name,Email,Phone_number,Type) values (110,'Swetha','swetha18@gmail.com',7490265512,'adult');
insert into Passengers (Passenger_id,Name,Email,Phone_number,Type) values (111,'Deepak','swetha18@gmail.com',7490265512,'child');
insert into Passengers (Passenger_id,Name,Email,Phone_number,Type) values (112,'Karthik','swetha18@gmail.com',7490265512,'child');
insert into Passengers (Passenger_id,Name,Email,Phone_number,Type) values (113,'John','henry89@gmail.com',7590147890,'child');
insert into Passengers (Passenger_id,Name,Email,Phone_number,Type) values (114,'Sekar','geetha13@gmail.com',9443009876,'child');
insert into Passengers (Passenger_id,Name,Email,Phone_number,Type) values (115,'Lily','cathy12@gmail.com',9451285679,'child');
insert into Passengers (Passenger_id,Name,Email,Phone_number,Type) values (116,'Andrew','cathy12@gmail.com',9451285679,'child');
insert into Passengers (Passenger_id,Name,Email,Phone_number,Type) values (117,'Arun','anil93@gmail.com',94896014593,'child');
insert into Passengers (Passenger_id,Name,Email,Phone_number,Type) values (118,'Dharshan','kumar45@gmail.com',9443078901,'child');
insert into Passengers (Passenger_id,Name,Email,Phone_number,Type) values (119,'Roshan','sharma001@gmail.com',9409012667,'child');
insert into Passengers (Passenger_id,Name,Email,Phone_number,Type) values (120,'Emily','cathy12@gmail.com',9451285679,'child');

