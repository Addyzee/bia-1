1. What is the best selling product in the whole company?

```sql
SELECT
    p.product_name,
    SUM(s.quantity) AS total_sold
FROM galaxy.sales s
JOIN galaxy.products p ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC;
```

2. What are the sales per store?

```sql
SELECT
s.store_id,
SUM(p.price * s.quantity) as total_amount
FROM galaxy.sales s
JOIN galaxy.stores st ON s.store_id = st.store_id
JOIN galaxy.products p ON  s.product_id = p.product_id
GROUP BY st.store_id, s.store_id
ORDER BY total_amount DESC;
```

3. Total revenue by product

```sql
SELECT
    p.product_name,
    SUM(s.quantity * p.price) AS total_revenue
FROM galaxy.sales s
JOIN galaxy.products p ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_revenue DESC;
```

4. What is the best selling product in each store?

```sql
WITH store_sales AS (
    SELECT
        s.store_id,
        st.store_address,
        s.product_id,
        p.product_name,
        SUM(s.quantity) AS total_quantity
    FROM galaxy.sales s
    JOIN galaxy.products p ON s.product_id = p.product_id
    JOIN galaxy.stores st ON s.store_id = st.store_id
    GROUP BY s.store_id, st.store_address, s.product_id, p.product_name
), ranked_sales AS (
    SELECT *,
           RANK() OVER (PARTITION BY store_id ORDER BY total_quantity DESC) AS rank
    FROM store_sales
)
SELECT
    store_address,
    product_name,
    total_quantity
FROM ranked_sales
WHERE rank = 1;

```

5. How much do we generate in sales from each of our suppliers?

```sql
SELECT
    sup.supplier_name,
    SUM(supplies.quantity * p.price) as total_worth
FROM galaxy.supplies supplies
JOIN galaxy.suppliers sup ON supplies.supplier_id = sup.supplier_id
JOIN galaxy.products p ON supplies.product_id = p.product_id
GROUP BY sup.supplier_name
ORDER BY total_worth DESC;

```
