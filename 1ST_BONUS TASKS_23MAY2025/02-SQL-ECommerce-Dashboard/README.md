# TASK: SQL Queries for E-Commerce Reporting Dashboard

## Title: Write SQL Queries for Business Intelligence.

### 1. Dataset Schema:

- `customers (customer_id, name, email, created_at)`
- `orders (order_id, customer_id, total_amount, order_date)`
- `order_items(order_item_id, order_id, product_id, quantity, price)`
- `products (product_id, name, category, price)`
- `site_visits (visit_id, visit_time)`

- Check File: `schema.sql`

### 2. Sample Dataset Ingestion:

- Check File: `data_ingestion.sql`

### 3. Check ALL TABLES and their values:

- Check File: `data_checker.sql`

---

### TASKS Completed ✅:

**1. List the top 10 customers by total spend.**

- Check File: `T1-top_10_customers_by_total_spend.sql`

**2. Generate a report of daily revenue and order count for the last 30 days.**

- Check File: `T2-daily_report_gen_ord_cnt_last_30_days.sql`

**3. Identify most sold products in the last 3 months.**

- Check File: `T3-most_sold_prods_last_3_months.sql`

**4. Calculate the conversion rate (orders/site visits) if given a site_visits table.**

- Check File: `T4-conversion-rate-calculate.sql`

**5. Show total revenue broken down by product category.**

- Check File: `T5-tot_rev_brok_dwn_by_prod_category.sql`
