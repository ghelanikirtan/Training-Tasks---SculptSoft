use business_intelligence;
WITH customer_spend AS (
    SELECT 
        c.customer_id,
        c.name,
        SUM(o.total_amount) AS total_spend
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.name
)
SELECT 
    customer_id,
    name,
    total_spend,
    DENSE_RANK() OVER (ORDER BY total_spend DESC) AS spend_rank
FROM customer_spend
LIMIT 10;
