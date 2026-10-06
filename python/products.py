from database import create_connection


def get_all_products():
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            p.product_id,
            p.product_name,
            c.category_name,
            p.price
        FROM Products p
        JOIN Categories c
            ON p.category_id = c.category_id
        WHERE p.is_active = TRUE
        ORDER BY p.price DESC;
    """

    cursor.execute(query)

    products = cursor.fetchall()

    for product in products:
        print(product)

    cursor.close()
    connection.close()

def add_product(name, category_id, price):
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO Products
        (product_name, category_id, price)
        VALUES (%s, %s, %s)
    """

    values = (name, category_id, price)

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    print("Product added successfully.")

def update_product(product_id, name, price):
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        UPDATE Products
        SET product_name = %s,
            price = %s
        WHERE product_id = %s
    """

    values = (name, price, product_id)

    cursor.execute(query, values)
    connection.commit()

    print(f"{cursor.rowcount} product updated.")

    cursor.close()
    connection.close()

def delete_product(product_id):
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        DELETE FROM Products
        WHERE product_id = %s
    """

    cursor.execute(query, (product_id,))
    connection.commit()

    print(f"{cursor.rowcount} product deleted.")

    cursor.close()
    connection.close()

def deactivate_product(product_id):
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        UPDATE Products
        SET is_active = FALSE
        WHERE product_id = %s
    """

    cursor.execute(query, (product_id,))
    connection.commit()

    if cursor.rowcount == 0:
        print("Product not found or already inactive.")
    else:
        print("Product deactivated successfully.")

    cursor.close()
    connection.close()

'''get_all_products()
add_product("HP EliteBook 840", 1, 780.00)
update_product(31, "HP EliteBook 840 G8", 800.00)'''
