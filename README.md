API Documentation
This API provides CRUD (Create, Read, Update, Delete) operations for managing persons.

Getting Started
Prerequisites
Before you begin, ensure you have met the following requirements:

Node.js and npm installed.
MongoDB server running and accessible.
Installation
To install and run the API, follow these steps:

Clone the repository:
git clone https://github.com/chizycodes/simple-api-hngx.git
Navigate to the project directory:
cd your-api
Install the dependencies:
npm install
Configure environment variables by creating a .env file in the root directory with the following content:
MONGO_URI=your_mongodb_connection_string_here
PORT=5000
Start the server:
npm start
The API should now be running on http://localhost:8000.

Usage
Endpoints
Create a New Person
Endpoint: POST /api/persons
Description: Create a new person.
Request Body:
name (string, required): The name of the person.
Fetch Details of a Person
Endpoint: GET /api/persons/:id
Description: Fetch details of a person by their name or ID.
Path Parameters:
id (string, required): The unique identifier of the person.
Update Details of an Existing Person
Endpoint: PUT /api/persons/:id
Description: Update details of an existing person by their ID.
Path Parameters:
id (string, required): The unique identifier of the person.
Request Body:
name (string, required): The updated name of the person.
Remove a Person
Endpoint: DELETE /api/persons/:id
Description: Remove a person by their ID.
Path Parameters:
id (string, required): The unique identifier of the person.
Request Formats
All request data must be sent in JSON format.
Include the required fields in the request body.
Response Formats
All responses are in JSON format.
Successful responses have a success field set to true and include the requested data.
Error responses have a success field set to false and include an error message.
Examples
Here are some sample API usage scenarios:

Create a New Person:
POST /api

Request Body:
{
  "name": "John Doe"
}
Fetch Details of a Person:
GET /api/123456
GET /api/John Doe

Response:
{
  "success": true,
  "data": {
    "_id": "123456",
    "name": "John Doe"
  }
}
Update Details of an Existing Person:
PATCH /api/123456

Request Body:
{
  "name": "Jane Doe"
}
Remove a Person:
DELETE /api/123456
Demo
The API is live at https://stage-two-d2n3.onrender.com/api

API documentation with examples here

Version: 1.0.0
License: MIT
Author: Adebiyi OLuwafemi
