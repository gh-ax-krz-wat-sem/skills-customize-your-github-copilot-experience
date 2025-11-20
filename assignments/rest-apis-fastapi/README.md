# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you will learn how to build a RESTful API using FastAPI, a modern Python web framework. You'll create endpoints to manage a simple task management system with full CRUD (Create, Read, Update, Delete) operations.

## 📝 Tasks

### 🛠️	Create a Basic FastAPI Application

#### Description
Set up a basic FastAPI application with a root endpoint that returns a welcome message. You'll also learn how to run the development server and test your API using the automatic documentation.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance
- Define a GET endpoint at the root path ("/") that returns a welcome message
- Run the application using uvicorn with auto-reload enabled
- Be accessible at http://localhost:8000
- Display interactive API documentation at http://localhost:8000/docs


### 🛠️	Implement Task Management Endpoints

#### Description
Build a complete REST API for managing tasks. Each task should have an ID, title, description, and completion status. Implement all CRUD operations following REST API best practices.

#### Requirements
Completed program should:

- Define a Task data model using Pydantic with fields: id (int), title (str), description (str), completed (bool)
- Create a GET /tasks endpoint to retrieve all tasks
- Create a GET /tasks/{task_id} endpoint to retrieve a specific task by ID
- Create a POST /tasks endpoint to add a new task
- Create a PUT /tasks/{task_id} endpoint to update an existing task
- Create a DELETE /tasks/{task_id} endpoint to remove a task
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Handle error cases gracefully (e.g., task not found)


### 🛠️	Add Data Validation and Error Handling

#### Description
Enhance your API with proper input validation and custom error responses. Learn how to use FastAPI's built-in validation features and create meaningful error messages for API consumers.

#### Requirements
Completed program should:

- Validate that task titles are between 3 and 100 characters long
- Validate that descriptions are not empty
- Return 404 status code with a custom error message when a task is not found
- Return 400 status code for invalid input data
- Use FastAPI's HTTPException for error handling
- Include helpful error messages in all error responses
