# ERP Sales & Inventory Management System

A small ERP-style Sales and Inventory Management system developed with Python and MySQL.

The project demonstrates database design, SQL queries, CRUD operations, transaction management, inventory control, and business reporting.

## Technologies

* Python 3.11
* MySQL
* MySQL Connector/Python
* SQL
* PyCharm

## Features

### Product Management

* List active products
* Add products
* Update products
* Deactivate products
* Product categories
* Product pricing

Products are deactivated instead of being permanently deleted, allowing historical sales data to remain intact.

### Order Management

* Create orders
* Validate customers
* Validate products
* Check inventory availability
* Create order details
* Automatically update inventory
* Calculate order totals
* List orders

### Reports

* Customer sales report
* Low-stock products
* Best-selling products
* Total sales
* Customer sales using SQL View

## Database Structure

The database contains the following main tables:

```text
Categories
    │
    └── Products
            │
            └── Inventory

Customers
    │
    └── Orders
            │
            └── OrderDetails
                    │
                    └── Products
```

### Main Tables

* `Categories`
* `Products`
* `Customers`
* `Orders`
* `OrderDetails`
* `Inventory`

## SQL Concepts Used

The project demonstrates several practical SQL concepts:

* Primary Keys
* Foreign Keys
* Constraints
* JOIN
* GROUP BY
* HAVING
* Aggregate Functions
* Subqueries
* Views
* ORDER BY
* Filtering with WHERE
* INSERT
* UPDATE
* Transactions
* COMMIT
* ROLLBACK

## Transaction Management

Order creation is handled as a transaction.

When creating an order, the system:

1. Validates the customer.
2. Checks the product and inventory.
3. Validates the requested quantity.
4. Creates the order.
5. Creates the order detail.
6. Updates the inventory.
7. Commits the transaction.

If an error occurs, the transaction is rolled back.

```text
Create Order
     │
     ├── Validate Customer
     │
     ├── Check Product & Stock
     │
     ├── Create Order
     │
     ├── Create Order Details
     │
     ├── Update Inventory
     │
     └── COMMIT
             │
          Error?
             │
          ROLLBACK
```

## Project Structure

```text
ERP-Sales-Inventory/
│
├── python/
│   ├── database.py
│   ├── products.py
│   ├── orders.py
│   ├── reports.py
│   └── main.py
│
├── sql/
│   └── reports.sql
│
├── .env.example
├── .gitignore
└── README.md
```

## Configuration

Database credentials are not stored directly in the source code.

The application reads the following environment variables:

```text
DB_HOST
DB_USER
DB_PASSWORD
DB_NAME
```

Example:

```text
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password_here
DB_NAME=sales_inventory
```

For security reasons, the actual database password should not be committed to the repository.

## Running the Project

### 1. Create the database

Create a MySQL database named:

```sql
CREATE DATABASE sales_inventory;
```

Create the required tables and sample data using the SQL scripts.

### 2. Configure database credentials

Set the following environment variables:

```text
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=sales_inventory
```

### 3. Install the required Python package

```bash
pip install mysql-connector-python
```

### 4. Run the application

Run:

```text
python/main.py
```

The application provides a command-line menu for managing products, orders, inventory, and reports.

## Example Reports

The system can generate reports such as:

* Total sales
* Customer purchase totals
* Best-selling products
* Low-stock products
* Completed orders

## Business Rules

Some important business rules implemented in the application:

* Order quantity must be greater than zero.
* An order cannot exceed available inventory.
* A customer must exist before an order can be created.
* A product must have inventory information before it can be ordered.
* Inventory is updated automatically after a successful order.
* Failed order operations are rolled back.
* Products are deactivated rather than permanently deleted.

## Future Improvements

Possible future improvements include:

* Supplier management
* Purchase orders
* Multiple warehouses
* Stock movement history
* Sales returns
* Purchase returns
* User authentication and roles
* Invoice management
* Payment management
* REST API
* Web-based interface
* Dashboard and data visualization

## Purpose

This project was developed as a practical demonstration of Python programming, relational database design, SQL querying, transaction management, and ERP-related business logic.
