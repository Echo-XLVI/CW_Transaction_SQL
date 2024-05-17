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
Begin ; 
		do $$
		BEGIN 
			update inventory 
			set body=body-1,wheel=wheel-1;

			update production
			set bicycle_count=bicycle_count+1;

			Exception 
				When others then  
-- 					Rollback;
					raise notice 'invalid data type';
		End ;
		$$ LANGUAGE plpgsql;
commit;

---------------------------------- Test
-- drop table inventory;
-- drop table production;
select * from inventory;
select * from production;