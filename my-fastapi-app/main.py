import logging

from fastapi import FastAPI

from endpoints.chat import ChatController
from endpoints.message import MessageController

# Configure logging settings (optional)
logging.basicConfig(level=logging.DEBUG)  # Set the desired log level

app = FastAPI(debug=True)

# Example of including a router
app.include_router(ChatController.router, prefix="/api/v1")
app.include_router(MessageController.router, prefix="/api/v1")

logging.info("Starting server...")


@app.get("/")
async def root():
    return {"message": "Bruce's App!"}
