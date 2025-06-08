
Instructions

Create a table called product_orders and a table called items. You decide which fields should be in each table, although make sure the items table has a column called price.

There should be a one to many relationship between the product_orders table and the items table. An order can have many items, but an item can belong to only one order.

Create a function that returns the total price for a given order.

Bonus :
Create a table called users.
There should be a one to many relationship between the users table and the product_orders table.
Create a function that returns the total price for a given order of a given user.

##########################################################################################################################################################################################


Here’s a complete SQL implementation based on your instructions, covering:

Creating the necessary tables and relationships
Writing a function to return the total price of an order
Bonus: Adding a users table and a function for total price per order per user
🧱 Step 1: Create Tables

✅ product_orders and items – One to Many
CREATE TABLE product_orders (
    id SERIAL PRIMARY KEY,
    order_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    order_id INT REFERENCES product_orders(id) ON DELETE CASCADE
);
🧠 Step 2: Function to return total price for an order

CREATE OR REPLACE FUNCTION get_order_total(order_id_input INT)
RETURNS NUMERIC AS $$
DECLARE
    total NUMERIC;
BEGIN
    SELECT SUM(price)
    INTO total
    FROM items
    WHERE order_id = order_id_input;

    RETURN COALESCE(total, 0);
END;
$$ LANGUAGE plpgsql;
🔍 Use COALESCE(total, 0) in case the order has no items.
⭐ Bonus: Add Users and connect to orders

✅ Create users table and link to product_orders
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE
);

-- Add user_id to product_orders
ALTER TABLE product_orders
ADD COLUMN user_id INT REFERENCES users(id) ON DELETE CASCADE;
🧠 Bonus Function: Get total price for an order of a user

CREATE OR REPLACE FUNCTION get_user_order_total(user_id_input INT, order_id_input INT)
RETURNS NUMERIC AS $$
DECLARE
    total NUMERIC;
BEGIN
    SELECT SUM(i.price)
    INTO total
    FROM items i
    JOIN product_orders po ON i.order_id = po.id
    WHERE po.id = order_id_input AND po.user_id = user_id_input;

    RETURN COALESCE(total, 0);
END;
$$ LANGUAGE plpgsql;
✅ Test Data (Optional)

-- Add users
INSERT INTO users (username) VALUES ('Alice'), ('Bob');

-- Add orders
INSERT INTO product_orders (user_id) VALUES (1), (1), (2);

-- Add items
INSERT INTO items (product_name, price, order_id)
VALUES 
('Book', 12.99, 1),
('Pen', 1.99, 1),
('Notebook', 5.50, 2),
('Bag', 20.00, 3);
✅ Example Queries

SELECT get_order_total(1);  -- returns 14.98
SELECT get_user_order_total(1, 1);  -- returns 14.98
SELECT get_user_order_total(2, 1);  -- returns 0, as order 1 doesn't belong to user 2
