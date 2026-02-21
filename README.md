# Internal Process API

Backend API built with FastAPI for managing internal processes and task workflows.

## Tech Stack

- Python 3.12+
- FastAPI
- Uvicorn
- python-dotenv
- uv (dependency management)

## Project Structure

```app/
 ├── core/        # Configuration and core logic
 ├── routers/     # API route definitions
 └── main.py      # FastAPI application entry point ```

## Environment Setup

1. Copy the example environment file:

cp .env.example .env

2. Install dependencies:

uv sync

3. Run the server:

uvicorn app.main:app --reload

## Health Check

GET /health

## API Documentation

Interactive Swagger UI available at:

/docs