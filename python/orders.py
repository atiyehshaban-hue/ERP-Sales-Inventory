from database import create_connection

def create_order(customer_id, product_id, quantity):

    connection = create_connection()
    cursor = connection.cursor()

    try:

        # Check customer
        query = """
            SELECT customer_id
            FROM Customers
            WHERE customer_id = %s
        """

        cursor.execute(query, (customer_id,))

        customer = cursor.fetchone()

        if customer is None:
            print("Customer not found.")
            return

        # Get product price and stock
        query = """
            SELECT
                p.price,
                i.stock_quantity
            FROM Products p
            JOIN Inventory i
                ON p.product_id = i.product_id
            WHERE p.product_id = %s
        """

        cursor.execute(query, (product_id,))

        product = cursor.fetchone()

        if product is None:
            print("Product not found or inventory does not exist.")
            return

        price = product[0]
        stock = product[1]

        # Validate quantity
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        if quantity > stock:
            print("Not enough stock.")
            return

        # Create order
        query = """
            INSERT INTO Orders
            (customer_id, order_date, status)
            VALUES (%s, CURDATE(), 'Completed')
        """

        cursor.execute(query, (customer_id,))

        order_id = cursor.lastrowid

        # Create order detail
        query = """
            INSERT INTO OrderDetails
            (order_id, product_id, quantity, unit_price)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (order_id, product_id, quantity, price)
        )

        # Update inventory
        query = """
            UPDATE Inventory
            SET stock_quantity = stock_quantity - %s
            WHERE product_id = %s
        """

        cursor.execute(
            query,
            (quantity, product_id)
        )

        connection.commit()

        print("\nOrder created successfully.")
        print(f"Order ID: {order_id}")
        print(f"Product: {product_id}")
        print(f"Quantity: {quantity}")
        print(f"Unit Price: {price}")
        print(f"Total: {quantity * price}")

    except Exception as e:

        connection.rollback()

        print("Error while creating order.")
        print(e)

    finally:

        cursor.close()
        connection.close()


def get_orders():

    connection = create_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            o.order_id,
            CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
            o.order_date,
            o.status,
            SUM(od.quantity * od.unit_price) AS total_amount
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
        ORDER BY o.order_id DESC;
    """

    cursor.execute(query)

    orders = cursor.fetchall()

    print("\nOrders")
    print("-" * 70)

    for order in orders:

        print(
            f"ID: {order[0]} | "
            f"Customer: {order[1]} | "
            f"Date: {order[2]} | "
            f"Status: {order[3]} | "
            f"Total: {order[4]}"
        )

    cursor.close()
    connection.close()