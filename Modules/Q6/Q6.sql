Create Database b_bank;

Create table account
(acc_id serial constraint pk_account_acc_id primary key,
 "name" varchar(40) not null,
 balance int not null 
);