use business_intelligence;

with total_revenue_by_category as (
	select 
		p.category,
        SUM(oi.quantity * oi.price) as total_revenue,
        SUM(oi.quantity * oi.price) / sum(SUM(oi.quantity * oi.price)) over () * 100 as revenue_percentage
    from 
		products as p
	join 
		order_items as oi 
	on p.product_id = oi.order_id
    group by p.category
)
select * from total_revenue_by_category order by total_revenue desc;
