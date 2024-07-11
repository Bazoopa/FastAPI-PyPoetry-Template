# main.py

import logging
from fastapi import FastAPI
from database import engine # Import engine and Base from database.py
from endpoints.chat import ChatController
from endpoints.message import MessageController

# Configure logging settings (optional)
logging.basicConfig(level=logging.DEBUG)  # Set the desired log level

# Initialize FastAPI app
app = FastAPI(debug=True)

# Example of including a router
app.include_router(ChatController.router, prefix="/api/v1")
app.include_router(MessageController.router, prefix="/api/v1")

logging.info("Starting server...")


# Create tables on startup
@app.on_event("startup")
async def startup():
    logging.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    logging.info("Database tables created.")


@app.get("/")
async def root():
    return {"message": "Bruce's App!"}
