import mysql.connector
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Allowing CORS for all origins (you can restrict this to specific domains)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database configuration
config = {
    'user': 'wedding_app',
    'password': 'Busam_2023!',
    'host': 'localhost',
    'raise_on_warnings': True
}

# Define a Pydantic model for product data
class Product(BaseModel):
    id: int
    name: str
    image_url: str
    video_url: str
    specs: str

# Function to load sample products (remains unchanged)
def load_sample_products():
    cursor = None
    conn = None
    sample_products = [
        {
            "id": 10,
            "name": "iPhone 14",
            "image_url": "https://example.com/images/iphone14.jpg",
            "video_url": "https://example.com/videos/iphone14.mp4",
            "specs": "6.1-inch display, A15 Bionic chip, Dual-camera system"
        },
        {
            "id": 11,
            "name": "MacBook Air M2",
            "image_url": "https://example.com/images/macbookairm2.jpg",
            "video_url": "https://example.com/videos/macbookairm2.mp4",
            "specs": "13.3-inch Retina display, M2 chip, 18 hours battery life"
        },
        {
            "id": 12,
            "name": "iPad Pro 11",
            "image_url": "https://example.com/images/ipadpro11.jpg",
            "video_url": "https://example.com/videos/ipadpro11.mp4",
            "specs": "11-inch Liquid Retina display, M1 chip, 120Hz refresh rate"
        }
    ]

    try:
        conn = mysql.connector.connect(**config, database='apple_products')
        cursor = conn.cursor()

        # Drop existing data from the products table
        cursor.execute("DELETE FROM products;")  # This will remove all existing records

        for product in sample_products:
            cursor.execute("""
                INSERT INTO products (id, name, image_url, video_url, specs) 
                VALUES (%s, %s, %s, %s, %s)
            """, (product['id'], product['name'], product['image_url'], product['video_url'], product['specs']))

        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

# New API endpoint to get multiple products by IDs
@app.get("/api/products/", response_model=List[Product])
async def get_multiple_products(product_ids: str):
    ids = [int(id) for id in product_ids.split(",")]

    cursor = None
    conn = None
    
    try:
        conn = mysql.connector.connect(**config, database='apple_products')
        cursor = conn.cursor(dictionary=True)

        # Create a placeholder string for the SQL query
        placeholders = ', '.join(['%s'] * len(ids))
        
        # Fetch multiple products based on IDs
        query = f"SELECT * FROM products WHERE id IN ({placeholders})"
        
        cursor.execute(query, ids)
        
        products = cursor.fetchall()
        
        if not products:
            raise HTTPException(status_code=404, detail="No products found for the given IDs")

        return products  # FastAPI will automatically convert this to JSON response.
    
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=str(err))
    
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    load_sample_products()  # Load sample products when the app starts

    import uvicorn  # Importing Uvicorn for running the FastAPI app

    # Run the app on port 8000 (you can change this to any port you prefer)
    uvicorn.run(app, host="127.0.0.1", port=8000)