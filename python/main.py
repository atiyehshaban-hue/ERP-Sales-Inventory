from products import (
    get_all_products,
    add_product,
    update_product,
    deactivate_product
)

from reports import (
    customer_sales_report,
    low_stock_report,
    best_selling_products,
    total_sales_report,
    customer_sales_view_report
)

from orders import (
    create_order,
    get_orders
)

def show_menu():
    print("\n" + "=" * 40)
    print("ERP Sales & Inventory Management")
    print("=" * 40)

    print("1. List Products")
    print("2. Add Product")
    print("3. Update Product")
    print("4. Deactivate Product")
    print("5. Customer Sales Report")
    print("6. Low Stock Report")
    print("7. Best-Selling Products")
    print("8. Create Order")
    print("9. List Orders")
    print("10. Customer Sales Report - View")
    print("11. Total Sales Report")
    print("12. Exit")

def get_integer_input(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid number.")

def get_float_input(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")
def main():

    while True:

        show_menu()

        choice = input("\nEnter your choice: ")

        try:

            if choice == "1":

                get_all_products()

            elif choice == "2":

                '''name = input("Product name: ")
                category_id = int(input("Category ID: "))
                price = float(input("Price: "))'''

                name = input("Product name: ")
                category_id = get_integer_input("Category ID: ")
                price = get_float_input("Price: ")

                add_product(name, category_id, price)

                add_product(name, category_id, price)

            elif choice == "3":

                '''product_id = int(input("Product ID: "))
                name = input("New product name: ")
                price = float(input("New price: "))'''

                product_id = get_integer_input("Product ID: ")
                name = input("New product name: ")
                price = get_float_input("New price: ")

                update_product(product_id, name, price)

                update_product(product_id, name, price)


            elif choice == "4":

                product_id = get_integer_input("Product ID: ")

                deactivate_product(product_id)


            elif choice == "5":

                customer_sales_report()


            elif choice == "6":

                low_stock_report()


            elif choice == "7":

                best_selling_products()


            elif choice == "8":

                customer_id = get_integer_input("Customer ID: ")

                product_id = get_integer_input("Product ID: ")

                quantity = get_integer_input("Quantity: ")

                create_order(customer_id, product_id, quantity)


            elif choice == "9":

                get_orders()


            elif choice == "10":

                customer_sales_view_report()


            elif choice == "11":

                total_sales_report()


            elif choice == "12":

                print("Goodbye!")

                break


            else:

                print("Invalid choice. Please select 1-12.")

        except ValueError:

            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()