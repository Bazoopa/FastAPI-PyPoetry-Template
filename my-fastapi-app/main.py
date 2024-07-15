import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from endpoints.chat import ChatController
from endpoints.message import MessageController

logging.basicConfig(level=logging.DEBUG)

app = FastAPI(debug=True, host="0.0.0.0")

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000",
                   "http://92.26.154.79",
                   "*"],  # Adjust based on your frontend URL
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Example of including routers
app.include_router(ChatController.router, prefix="/api/v1")
app.include_router(MessageController.router, prefix="/api/v1")

logging.info("Starting server...")#

@app.get("/")
async def root():
    return {"message": "Bruce's App!"}
