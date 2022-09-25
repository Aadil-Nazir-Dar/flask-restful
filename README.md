   ABOUT database
create database  Application.
create table user values id primary key, name ,age 
create table cars values id, brand, colour, mileage 
foreign key user_id


    Operations
get 
post
update
delete

End points

server address +, '/users',endpoint ='users')

server addrress +'/cars',endpoint='cars')

server address + '/user/<int:id>', endpoint='user')

