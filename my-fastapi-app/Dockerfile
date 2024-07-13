# Dockerfile for FastAPI app
FROM python:3.9-slim

# Install Poetry
RUN pip install poetry

WORKDIR /app

# Copy only the poetry files initially to leverage Docker cache
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-root

# Copy the rest of the application code
COPY . .

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
