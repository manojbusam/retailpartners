# iContent Product Data API

This project sets up a FastAPI application that interacts with a MySQL database to manage product data.

## Setup Instructions

1. **Execute the Setup Script**:
   To create the database and load sample data into it, run the following command in your terminal:

   ```bash
   ./setup.sh
   ```

2. **Access the API**:
   After running the setup script, you can view the product data by navigating to:

   ```
   http://127.0.0.1:8000/api/products
   ```
![Screenshot 2024-10-24 at 4 58 15 PM](https://github.com/user-attachments/assets/794e6052-1952-4c78-a96e-3f66ba8dcdca)

## SQL Commands

If you need to manually create the database and table, you can use the following SQL commands. These commands are available in the `apple_product.product.sql` file:

```sql
-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS apple_products;

-- Use the newly created database
USE apple_products;

-- Create the products table if it doesn't exist
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    image_url VARCHAR(255),
    video_url VARCHAR(255),
    specs TEXT
);

-- Grant privileges to the wedding_app user on the apple_products database
GRANT ALL PRIVILEGES ON apple_products.* TO 'wedding_app'@'localhost';

-- Flush privileges to ensure that they are applied
FLUSH PRIVILEGES;
```
![Screenshot 2024-10-24 at 4 59 12 PM](https://github.com/user-attachments/assets/4a4d6060-615b-4f16-a46e-6a51bba87ea1)


## Notes

- Ensure that your MySQL server is running before executing the setup script.
- Modify any necessary configurations in your FastAPI application as needed.


### Summary

- The `README.md` includes instructions for executing the `setup.sh` script and accessing the API.
- It also contains SQL commands for manually creating the database and table, along with granting privileges.
- Make sure to save this content in a file named `README.md` in your project directory.

Feel free to ask if you need any more modifications or additional information!
