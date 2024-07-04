# FastAPI-Template
A template for other FastAPI projects so I can create new projects quickly.

# Useful commands - For my own reference:
To start the main.py server:
 - uvicorn main:app --reload

To get the interactive API documentation (faster than postman):
 -  http://127.0.0.1:8000/docs
 - http://127.0.0.1:8000/redoc

To show Schema:
 - http://127.0.0.1:8000/openapi.json


# REST Reminders for myself:
When building APIs, you normally use these specific HTTP methods to perform a specific action.

Normally you use:

 - POST: to create data.
 - GET: to read data.
 - PUT: to update data.
 - DELETE: to delete data.

..and the more exotic ones:

 - OPTIONS
 - HEAD
 - PATCH
 - TRACE

Creating a path operations (Endpoints)
"Path" here refers to the last part of the URL starting from the first /.

So, in a URL like:

https://example.com/items/foo
...the path would be:

/items/foo