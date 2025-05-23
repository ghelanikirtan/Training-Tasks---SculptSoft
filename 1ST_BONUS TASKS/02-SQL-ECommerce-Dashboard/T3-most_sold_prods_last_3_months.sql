use business_intelligence;

WITH most_sold_products as (
	select 
    p.product_id,
    p.name,
    SUM(oi.quantity) as total_quantities_sold
    from products as p
    join order_items as oi on p.product_id = oi.product_id
    join orders as o on o.order_id = oi.order_id
    where o.order_date >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH)
    group by p.product_id, p.name
) 
select 
	product_id,
    name, 
    total_quantities_sold,
    RANK() over (order by total_quantities_sold desc) as quant_rank
from most_sold_products;

