
SELECT products.name AS product_name,
 EXTRACT(YEAR FROM sales.date)::integer as year,
 EXTRACT(MONTH FROM sales.date)::integer as month,
 EXTRACT(day FROM sales.date)::integer as day,
 SUM(products.price * sales_details.count) AS total
FROM products
LEFT JOIN sales_details ON products.id = sales_details.product_id
LEFT JOIN sales ON sales_details.sale_id = sales.id
GROUP BY product_name, ROLLUP (year, month, day)
ORDER BY product_name, year, month, day;