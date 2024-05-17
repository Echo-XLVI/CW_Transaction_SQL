---------------------------------- Creation
-- Create database manufacturing;

-- Create table inventory
-- (body int not null,
--  wheel int not null
-- );

-- Create table production
-- (bicycle_count int
-- );
---------------------------------- Insertion
-- insert into inventory values(120,180);

-- insert into production values(0);

---------------------------------- Transaction
Begin;
Savepoint bi_created;

	update inventory 
	set body=body-1,wheel=wheel-1;
	
Savepoint s1;

	update production
	set bicycle_count=bicycle_count+1;
	


-- select * from inventory;
select * from production;
Rollback To s1;
Rollback To bi_created ;


---------------------------------- Test
-- drop table inventory;
-- drop table production;
select * from inventory;
select * from production;