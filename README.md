# iContent Product Data API

This project sets up a iContent API that Reads a Apple database to GET Product(s) details using FastAPI.

![Screenshot 2024-10-24 at 5 23 03 PM](https://github.com/user-attachments/assets/48b9be32-88c4-4405-80cc-95ad22d6e654)


## 1. Introduction to Apple iContent API

The iContent Product Data API provides a seamless way to access product information from an Apple database. This API is designed for developers looking to integrate product data into their applications, enabling them to retrieve images, videos, specifications, and marketing content efficiently.

### Overview and Use Cases
- **E-commerce Platforms**: Integrate product details directly into online stores.
- **Mobile Applications**: Fetch and display product information dynamically.
- **Marketing Tools**: Use product data for promotional campaigns and analytics.

### Prerequisites for Integration
How REST Works: RESTful APIs utilize standard HTTP methods to perform operations on resources:
- GET: Retrieve resource(s).
- POST: Create a new resource.
- PUT: Update an existing resource.
- DELETE: Remove a resource.



---

## 2. Authentication & Authorization

### API Key Generation
To secure your API, generate an API key that must be included in the header of each request.

### OAuth 2.0 Implementation
For more secure applications, consider implementing OAuth 2.0 to manage user authentication and authorization.

---

## 3. API Endpoints

### Product Data Retrieval
The API provides endpoints to retrieve detailed information about products, including:
- Images
- Videos
- Marketing copy
- Specifications

#### Example Endpoint:
- **Get Specific Product Details**:

`GET http://iContent.apple.com/api/products/?product_ids={productID}`
- **Get Specific Products Details**:

`GET http://iContent.apple.com/api/products/?product_ids={productID1,productID2..productIDn}`

---

## 4. Request and Response Formats

### JSON Payloads
The API uses JSON format for both requests and responses.

#### Sample Request:
```http
GET /api/products/1 HTTP/1.1
Host: 127.0.0.1:8000
```

#### Sample Response:
```json
{
    "id": 1,
    "name": "iPhone 14",
    "image_url": "https://example.com/images/iphone14.jpg",
    "video_url": "https://example.com/videos/iphone14.mp4",
    "specs": "6.1-inch display, A15 Bionic chip, Dual-camera system"
}
```

---

## 5. Error Handling

### Common Error Codes and Troubleshooting
- **404 Not Found**: The requested product does not exist.
- **500 Internal Server Error**: An error occurred on the server side.
  
Refer to the documentation for detailed error messages and troubleshooting steps.

---

## 6. Versioning & Updates

### API Versioning Strategy
To maintain backward compatibility, the API will use versioning in the URL:
```
http://127.0.0.1:8000/v1/api/products
```
This allows developers to adapt to changes without breaking existing implementations.

---

## 7. Rate Limiting

### API Call Limits and Optimization Best Practices
To ensure fair usage of resources:
- Limit the number of requests per minute per user.
- Implement caching strategies to reduce redundant calls.

---

## 8. Security Guidelines

### Data Encryption and Compliance Measures
- Use HTTPS for all communications to encrypt data in transit.
- Regularly update your dependencies to mitigate vulnerabilities.
- Follow compliance measures such as GDPR when handling user data.

## Setup Instructions

1. **Execute the Setup Script**:
   To create the database and load sample data into it, run the following command in your terminal:

   ```bash
   ./setup.sh
   ```

2. **Access the API**:
   After running the setup script, you can view the product data(PDP Details) by navigating to:

   ```
   http://127.0.0.1:8000/api/products/{productID}
   ```

   or

   ```
   http://127.0.0.1:8000/api/products/11
   ```
   ![Screenshot 2024-10-24 at 5 10 43 PM](https://github.com/user-attachments/assets/e551a2ca-d787-44c9-96cb-b387cd807e3b)


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

SELECT * FROM apple_products.products;
```
![Screenshot 2024-10-24 at 5 13 49 PM](https://github.com/user-attachments/assets/ecabcc25-ec77-4237-a57e-10c0ab805235)



## Notes

- Ensure that your MySQL server is running before executing the setup script.
- Modify any necessary configurations in your FastAPI application as needed.
