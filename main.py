import logging
from fastapi import FastAPI
from myApp.controllers import ChatController

# Configure logging settings (optional)
logging.basicConfig(level=logging.DEBUG)  # Set the desired log level

app = FastAPI(debug=True)

# Example of including a router
app.include_router(ChatController.router, prefix="/api/v1")

logging.info("Starting server...")


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
