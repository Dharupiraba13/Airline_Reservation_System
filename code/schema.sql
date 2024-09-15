
/* Drop table statements */
drop table Tickets_have_Charges;
drop table Tickets;
drop table fly;
drop table Pilots;
drop table have_Seats;
drop table Costs;
drop table Charges;
drop table Passengers;
drop table Flights;
drop table departfrom_Routes_arriveto;
drop table Airports;
drop table Aircrafts;
/* Create table statements */

create table Aircrafts (
  Aircraft_id varchar(128) primary key,
  Capacity integer not null,
  Company varchar(128) not null
);

create table Airports(
  Airport_name varchar(128) unique,
  Lat varchar(128),
  Long varchar(128),
  City varchar(128),
  State varchar(128),
  Country varchar(128),
  Iata_code varchar(128),
  primary key(Lat,Long)
);

create table departfrom_Routes_arriveto(
  Route_id integer primary key,
  Destination varchar(128) not null,
  Source varchar(128) not null,
  Route varchar(128) unique not null,
  Stops integer,
  Foreign key(Source) references Airports(Airport_name),
  Foreign key(Destination) references Airports(Airport_name)
);

create table Flights(
  Flight_id integer primary key,
  Flight_name varchar(128) not null,
  Route_id integer not null,
  Departure_date date not null,
  Departure_time time not null,
  Duration varchar(32) not null,
  Aircraft_id varchar(128) not null,
  Status varchar(128),
  Foreign key(Route_id) references departfrom_Routes_arriveto(Route_id),
  Foreign key(Aircraft_id) references Aircrafts(Aircraft_id)
);

create table Passengers (
  Passenger_id integer primary key,
  Name varchar(128) not null,
  Email varchar(128) not null,
  Phone_number varchar(128) not null,
  Type varchar(128) not null
);

create table Charges (
  Charge_id integer primary key,
  Charge_type varchar(128) not null,
  Charge_amount integer not null
);

create table Costs (
  Cost_id integer primary key,
  Amount integer not null,
  Type varchar(128) not null,
  Class varchar(128),
  Location varchar(128)
);


create table have_Seats (
  Seat_number varchar(128),
  Flight_id integer,
  Cost_id integer not null,
  primary key(Flight_id,Seat_number),
  Foreign key (Flight_id) references Flights(Flight_id) on delete cascade,
  Foreign key (Cost_id) references Costs(Cost_id)
);

create table Pilots (
  Pilot_id integer primary key,
  Pilot_name varchar(128) not null
);

create table fly (
  Flight_id integer,
  Pilot_id integer,
  primary key(Flight_id, Pilot_id),
  Foreign key(Flight_id) references Flights(Flight_id),
  Foreign key(Pilot_id) references Pilots(Pilot_id)
);

create table Tickets (
  Ticket_id integer primary key,
  Passenger_id integer not null,
  Cost_id integer not null,
  Seat_number varchar(128) not  null,
  Flight_id integer not null,
  unique(Passenger_id,Seat_number,Flight_id),
  Foreign key(Passenger_id) references Passengers(Passenger_id),
  Foreign key(Cost_id) references Costs(Cost_id),
  Foreign key (Flight_id,Seat_number) references have_Seats(Flight_id,Seat_number)
);

create table Tickets_have_Charges (
 Ticket_id integer,
 Charge_id integer,
 primary key(Ticket_id, Charge_id),
 Foreign key(Ticket_id) references Tickets(Ticket_id),
 Foreign key(Charge_id) references Charges(Charge_id)
);
