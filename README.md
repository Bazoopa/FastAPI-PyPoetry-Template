# FastAPI-Template
A template for other FastAPI projects so I can create new projects quickly.

This template will just have a database and endpoints that can be accessed by a client like
postman

# Design

Current setup:
 - Controllers, end point for API calls
 - Services, the business logic for the controllers
 - DAOs, Interacts with the database and returns data structures for service layer
 - DTOs, Service layer transforms domain objects into DTOs for presentation or transfer

# Useful commands - For my own reference:
To start the main.py server:
 - uvicorn main:app --reload

# API endpoint URL:
 - http://localhost:8000/api/v1/

# How to not push SQL Username and Password to git:
 - Make the password an environment variable?

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

# Python Poetry useful stuff:

Add a dependency:
 - poetry add ...

install dependencies:
 - poetry install

Get Python environment information:
 - poetry env info



# List of Dependencies:

- FastAPi
- Uvicorn
- 


# Useful Pages:

Async:
https://fastapi.tiangolo.com/async/


# Current setup (delete this later)
crud.py acts like a service layer
database.py connects to the DB
main.py acts as a controller
models.py acts like a model
schemas.py acts like a DTO?


# Current plan:
- Build an open chat system, get it working, and host it with docker (this is essentially the template)
- When that works, create a log in system for it
- When that works, create the same but for a to-do list
- When that works, create a calendar system