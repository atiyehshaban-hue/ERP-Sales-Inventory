from database import create_connection


def customer_sales_report():
    connection = create_connection()
    cursor = connection.cursor()

    query = """
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
    """

    cursor.execute(query)

    results = cursor.fetchall()

    print("\nCustomer Sales Report")
    print("-" * 50)

    for row in results:
        print(
            f"ID: {row[0]} | "
            f"Customer: {row[1]} | "
            f"Total Purchase: {row[2]}"
        )

    cursor.close()
    connection.close()

def low_stock_report():
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            p.product_id,
            p.product_name,
            i.stock_quantity
        FROM Products p
        JOIN Inventory i
            ON p.product_id = i.product_id
        WHERE i.stock_quantity < 10
        ORDER BY i.stock_quantity ASC;
    """

    cursor.execute(query)

    results = cursor.fetchall()

    print("\nLow Stock Report")
    print("-" * 50)

    for row in results:
        print(
            f"ID: {row[0]} | "
            f"Product: {row[1]} | "
            f"Stock: {row[2]}"
        )

    cursor.close()
    connection.close()

def best_selling_products():
    connection = create_connection()
    cursor = connection.cursor()

    query = """
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
    """

    cursor.execute(query)

    results = cursor.fetchall()

    print("\nBest-Selling Products")
    print("-" * 50)

    for row in results:
        print(
            f"ID: {row[0]} | "
            f"Product: {row[1]} | "
            f"Quantity Sold: {row[2]}"
        )

    cursor.close()
    connection.close()

def total_sales_report():
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            SUM(od.quantity * od.unit_price) AS total_sales,
            COUNT(DISTINCT o.order_id) AS completed_orders
        FROM Orders o
        JOIN OrderDetails od
            ON o.order_id = od.order_id
        WHERE o.status = 'Completed';
    """

    cursor.execute(query)

    result = cursor.fetchone()

    print("\nTotal Sales Report")
    print("-" * 50)

    print(f"Total Sales: {result[0]}")
    print(f"Completed Orders: {result[1]}")

    cursor.close()
    connection.close()

def customer_sales_view_report():
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            customer_id,
            customer_name,
            total_purchase
        FROM customer_sales_report
        ORDER BY total_purchase DESC;
    """

    cursor.execute(query)

    results = cursor.fetchall()

    print("\nCustomer Sales Report - View")
    print("-" * 50)

    for row in results:
        print(
            f"ID: {row[0]} | "
            f"Customer: {row[1]} | "
            f"Total Purchase: {row[2]}"
        )

    cursor.close()
    connection.close()
def customer_sales_view_report():
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            customer_id,
            customer_name,
            total_purchase
        FROM customer_sales_report
        ORDER BY total_purchase DESC;
    """

    cursor.execute(query)

    results = cursor.fetchall()

    print("\nCustomer Sales Report - Using View")
    print("-" * 60)

    for row in results:
        print(
            f"ID: {row[0]} | "
            f"Customer: {row[1]} | "
            f"Total Purchase: {row[2]}"
        )

    cursor.close()
    connection.close()

'''low_stock_report()
customer_sales_report()'''