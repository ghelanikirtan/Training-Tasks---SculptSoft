use world;
show tables;
desc city;
desc country;
desc countrylanguage;
-- WINDOW FUNCTIONS SQL:

-- 1. AGGREGATION BASED [WINDOW FUNCTIONS]:
-- 1.1 count()
select COUNT(distinct ct.CountryCode) as TotalCountries
from city as ct;

-- 1.2 sum()
select CountryCode as COUNTRY, SUM(Population) as countrywise_population
from city
group by CountryCode;

select SUM(ct.Population) as NetPopulation
from city as ct;

-- 1.3 avg():
select ROUND(AVG(ct.Population)) as MEAN_POPULATION
from city as ct;

-- 1.4 min():
select * from city where Population = (select min(Population) as minimum_population from city);

-- 1.5 max():
select * from city where Population = (select MAX(Population) as minimum_population from city);

-- 2. VALUE BASED [WINDOW FUNCTIONS]:

-- 2.1 ROW_NUMBER() 
-- Used for assigning the row numbers 

select ROW_NUMBER() over (order by Population) as row_num ,CountryCode, Population Name
from city limit 10; 

-- partitioning row numbers country wise:
select ROW_NUMBER() over (partition by CountryCode order by Population) as row_num ,CountryCode, Name, Population 
from city limit 10; 

-- 2.2 RANK()
-- RANK() skips the integer when there's a condition for the same ranking arises.
-- city wise ranking
select RANK() over (order by Population desc) as POP_INDEX_RANK_CITY_WISE, Name, Population
from city limit 5;

-- country specific separate ranking
select RANK() over (partition by CountryCode order by Population desc) as POP_INDEX_RANK_INDIA, Name, Population
from city 
where CountryCode = 'IND';

select RANK() over (partition by CountryCode order by Population desc) as POP_INDEX_RANK_USA, Name, Population
from city 
where CountryCode = 'USA';

-- 2.3 dense_rank():
-- unlike rank() this function doesnot skip the integer in case of condition for multiple rows having same rank arises...

select DENSE_RANK() over (order by Population desc) as POP_INDEX_RANK_CITY_WISE, Name, Population
from city limit 5;

select DENSE_RANK() over (partition by CountryCode order by Population desc) as POP_INDEX_RANK_INDIA, Name, Population
from city 
where CountryCode = 'IND';

-- 2.4 percent_rank():
select PERCENT_RANK() over (order by Population desc) as POP_INDEX_RANK_CITY_WISE, Name, Population
from city limit 5;

select PERCENT_RANK() over (partition by CountryCode order by Population desc) as POP_INDEX_RANK_INDIA, Name, Population
from city 
where CountryCode = 'IND';

use world;
show tables;
desc city;
desc country;
desc countrylanguage;
-- WINDOW FUNCTIONS SQL:


-- 1. Aggregate Functions:

-- 1.1 count()
select COUNT(distinct ct.CountryCode) as TotalCountries
from city as ct;
-- 1.2 sum()
select CountryCode as COUNTRY, SUM(Population) as countrywise_population
from city
group by CountryCode;

select SUM(ct.Population) as NetPopulation
from city as ct;
-- 1.3 avg():
select ROUND(AVG(ct.Population)) as MEAN_POPULATION
from city as ct;
-- 1.4 min():
select * from city where Population = (select min(Population) as minimum_population from city);
-- 1.5 max():
select * from city where Population = (select MAX(Population) as minimum_population from city);


-- 2. VALUE BASED [WINDOW FUNCTIONS]:

-- 2.1 ROW_NUMBER() 
-- Used for assigning the row numbers 

select ROW_NUMBER() over (order by Population) as row_num ,CountryCode, Population Name
from city limit 10; 

-- partitioning row numbers country wise:
select ROW_NUMBER() over (partition by CountryCode order by Population) as row_num ,CountryCode, Name, Population 
from city limit 10; 


-- 2.2 RANK()
-- RANK() skips the integer when there's a condition for the same ranking arises.
-- city wise ranking
select RANK() over (order by Population desc) as POP_INDEX_RANK_CITY_WISE, Name, Population
from city limit 5;

-- country specific separate ranking
select RANK() over (partition by CountryCode order by Population desc) as POP_INDEX_RANK_INDIA, Name, Population
from city 
where CountryCode = 'IND' or CountryCode = 'USA';

-- 2.3 dense_rank():
-- unlike rank() this function doesnot skip the integer in case of condition for multiple rows having same rank arises...

select DENSE_RANK() over (order by Population desc) as POP_INDEX_RANK_CITY_WISE, Name, Population
from city limit 5;

select DENSE_RANK() over (partition by CountryCode order by Population desc) as POP_INDEX_RANK_INDIA, Name, Population
from city 
where CountryCode = 'IND';

-- 2.4 percent_rank():
select PERCENT_RANK() over (order by Population desc) as POP_INDEX_RANK_CITY_WISE, Name, Population
from city limit 5;

select PERCENT_RANK() over (partition by CountryCode order by Population desc) as POP_INDEX_RANK_INDIA, Name, Population
from city 
where CountryCode = 'IND';


-- 2.5 NTILE():
-- It is basically chunking...

-- this creates the grp of 50 cities as per the population...
select *, NTILE(50) over (order by Population) as grp_num
from city
where CountryCode = 'IND';


use sakila;
show tables;
desc payment;
select * from payment limit 3;


-- 3. ANALYTICAL BASED [WINDOW FUNCTIONS]:

-- 3.1. LAG():
-- The LAG() function is used to get value from the row that precedes the current row.
select payment_id, amount, LAG(last_update) over (order by payment_date) as lag_date_check
from payment;

-- 3.2 LEAD():
-- The LEAD() function is used to get value from a row that succeeds the current row.
select payment_id, amount, DATEDIFF(LEAD(payment_date) OVER (order by payment_date), last_update) + 1 as update_initial_days_diff
from payment;


use world;

-- 3.3 FIRST_VALUE():
-- will return the value from the first row in the window frame based on the specified order.
select ID, Name, first_value(Population) over (partition by CountryCode order by Population desc) 
from city;

-- 3.4 LAST_VALUE():
-- will return the value in the last row in the window frame based on the specified order
select ID, Name, last_value(Population) over (partition by CountryCode order by Population) 
from city;

-- 3.5 NTH_VALUE():
-- will return the value in the nth row in the window frame based on the specified order
select ID, Name, nth_value(Population, 20) over (partition by CountryCode order by Population range between unbounded preceding and unbounded following)
from city;


