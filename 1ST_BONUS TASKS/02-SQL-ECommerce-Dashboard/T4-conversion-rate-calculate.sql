use business_intelligence;

with conversions as (
	select 
		(select COUNT(*) from orders) as total_orders,
        (select COUNT(*) from site_visits) as total_site_visits
)
select (total_orders / total_site_visits) from conversions;
