import mysql.connector
from mysql.connector import errorcode
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

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



# Function to load sample products
def load_sample_products():
    cursor = None
    conn = None
    sample_products = [
        {
            "name": "iPhone 14",
            "image_url": "https://example.com/images/iphone14.jpg",
            "video_url": "https://example.com/videos/iphone14.mp4",
            "specs": "6.1-inch display, A15 Bionic chip, Dual-camera system"
        },
        {
            "name": "MacBook Air M2",
            "image_url": "https://example.com/images/macbookairm2.jpg",
            "video_url": "https://example.com/videos/macbookairm2.mp4",
            "specs": "13.3-inch Retina display, M2 chip, 18 hours battery life"
        },
        {
            "name": "iPad Pro 11",
            "image_url": "https://example.com/images/ipadpro11.jpg",
            "video_url": "https://example.com/videos/ipadpro11.mp4",
            "specs": "11-inch Liquid Retina display, M1 chip, 120Hz refresh rate"
        }
    ]

    try:
        conn = mysql.connector.connect(**config, database='apple_products')
        cursor = conn.cursor()

        for product in sample_products:
            cursor.execute("""
                INSERT INTO products (name, image_url, video_url, specs) 
                VALUES (%s, %s, %s, %s)
            """, (product['name'], product['image_url'], product['video_url'], product['specs']))

        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

# API endpoint to get product data
@app.get("/api/products", response_model=list[Product])
async def get_products():
    cursor = None
    conn = None
    try:
        conn = mysql.connector.connect(**config, database='apple_products')
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()

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