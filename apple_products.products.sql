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

SELECT * FROM apple_products.products;