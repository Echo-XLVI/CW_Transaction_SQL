-- CREATE database s_bank;

-- CREATE TABLE users(
--         user_id serial PRIMARY KEY, 
--         user_age int,
--         user_name varchar(50),
--         user_salary int
-- );

BEGIN;

INSERT INTO users(user_age,user_name,user_salary)
VALUES (18,'Harry',1000),
(18,'Ron',200),
(17,'Hermion',700);

rollback;

SELECT * FROM users;

drop table users;