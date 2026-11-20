-- Write your query below

SELECT customer_id, customer_name
FROM customers
--customers who got A
WHERE customer_id IN (
    SELECT customer_id
    FROM orders
    WHERE product_name = 'A'
)
--customers who got B
AND customer_id IN (
    SELECT customer_id 
    FROM orders
    WHERE product_name = 'B' -- single quotes for text value and double quotes for column name
)
--customers who did not get C but got A and B
AND customer_id NOT IN (
    SELECT customer_id
    FROM orders
    WHERE product_name = 'C'
)
-- question requirement:
ORDER BY customer_name;
