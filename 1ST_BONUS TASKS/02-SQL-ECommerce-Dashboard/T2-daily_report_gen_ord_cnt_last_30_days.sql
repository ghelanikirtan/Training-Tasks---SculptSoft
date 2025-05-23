use business_intelligence;
SELECT 
    order_date,
    SUM(total_amount) AS daily_revenue,
    COUNT(order_id) AS order_count
FROM orders
WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
  AND order_date < CURDATE()
GROUP BY order_date
ORDER BY order_date DESC;