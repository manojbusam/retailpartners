import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('product_db.sqlite')
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    price REAL
)
""")

# Load sample data
sample_data = [
    ('Product 1', 'Description for Product 1', 19.99),
    ('Product 2', 'Description for Product 2', 29.99),
]

cursor.executemany("INSERT INTO products (name, description, price) VALUES (?, ?, ?)", sample_data)
conn.commit()

# Function to get product data by ID
def get_product(product_id):
    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    return cursor.fetchone()

# Example usage
product_id = 1  # Change this to query different products
product_data = get_product(product_id)
if product_data:
    print(f"Product ID: {product_data[0]}, Name: {product_data[1]}, Description: {product_data[2]}, Price: ${product_data[3]}")
else:
    print("Product not found.")

# Close connection
cursor.close()
conn.close()