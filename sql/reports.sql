USE sales_inventory;


-- =====================================================
-- 1. PRODUCT REPORTS
-- =====================================================

-- 1.1 Products with their categories

SELECT
    p.product_id,
    p.product_name,
    c.category_name,
    p.price
FROM Products p
JOIN Categories c
    ON p.category_id = c.category_id
ORDER BY p.price DESC;

-- =====================================================
-- 2. ORDER REPORTS
-- =====================================================

-- 2.1 Orders with customer information

SELECT
    o.order_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    o.order_date,
    o.status
FROM Orders o
JOIN Customers c
    ON o.customer_id = c.customer_id
ORDER BY o.order_date;


-- 2.2 Order totals

SELECT
    order_id,
    SUM(quantity * unit_price) AS order_total
FROM OrderDetails
GROUP BY order_id
ORDER BY order_total DESC;


-- 2.3 Detailed order report

SELECT
    o.order_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    o.order_date,
    o.status,
    SUM(od.quantity * od.unit_price) AS order_total
FROM Orders o
JOIN Customers c
    ON o.customer_id = c.customer_id
JOIN OrderDetails od
    ON o.order_id = od.order_id
GROUP BY
    o.order_id,
    c.first_name,
    c.last_name,
    o.order_date,
    o.status
ORDER BY o.order_date;

-- =====================================================
-- 3. SALES REPORTS
-- =====================================================

-- 3.1 Total completed sales

SELECT
    SUM(od.quantity * od.unit_price) AS total_sales
FROM OrderDetails od
JOIN Orders o
    ON od.order_id = o.order_id
WHERE o.status = 'Completed';


-- 3.2 Best-selling products

SELECT
    p.product_id,
    p.product_name,
    SUM(od.quantity) AS total_quantity
FROM Products p
JOIN OrderDetails od
    ON p.product_id = od.product_id
JOIN Orders o
    ON od.order_id = o.order_id
WHERE o.status = 'Completed'
GROUP BY
    p.product_id,
    p.product_name
ORDER BY total_quantity DESC;

-- =====================================================
-- 4. CUSTOMER REPORTS
-- =====================================================

-- 4.1 Customer purchase report

SELECT
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    SUM(od.quantity * od.unit_price) AS total_purchase
FROM Customers c
JOIN Orders o
    ON c.customer_id = o.customer_id
JOIN OrderDetails od
    ON o.order_id = od.order_id
WHERE o.status = 'Completed'
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY total_purchase DESC;


-- 4.2 Customers with purchases greater than 1000

SELECT
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    SUM(od.quantity * od.unit_price) AS total_purchase
FROM Customers c
JOIN Orders o
    ON c.customer_id = o.customer_id
JOIN OrderDetails od
    ON o.order_id = od.order_id
WHERE o.status = 'Completed'
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
HAVING SUM(od.quantity * od.unit_price) > 1000
ORDER BY total_purchase DESC;

-- =====================================================
-- 5. INVENTORY REPORTS
-- =====================================================

-- 5.1 Low-stock products

SELECT
    p.product_id,
    p.product_name,
    i.stock_quantity
FROM Products p
JOIN Inventory i
    ON p.product_id = i.product_id
WHERE i.stock_quantity < 10
ORDER BY i.stock_quantity ASC;

-- =====================================================
-- 6. ADVANCED QUERIES
-- =====================================================

-- 6.1 Products with price above average

SELECT
    product_id,
    product_name,
    price
FROM Products
WHERE price > (
    SELECT AVG(price)
    FROM Products
)
ORDER BY price DESC;

-- =====================================================
-- 7. VIEWS
-- =====================================================

-- 7.1 Customer sales report view

CREATE OR REPLACE VIEW customer_sales_report AS
SELECT
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    SUM(od.quantity * od.unit_price) AS total_purchase
FROM Customers c
JOIN Orders o
    ON c.customer_id = o.customer_id
JOIN OrderDetails od
    ON o.order_id = od.order_id
WHERE o.status = 'Completed'
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name;


-- View result

SELECT *
FROM customer_sales_report
ORDER BY total_purchase DESC;