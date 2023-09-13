# API Documentation
API documentation with examples (https://documenter.getpostman.com/view/23522029/2s9YC4VCwy)


This API provides CRUD (Create, Read, Update, Delete) operations for managing persons.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

-a virtual environment

### Installation

To install and run the API, follow these steps:

1. Clone the repository:

```
git clone https://github.com/shabzynana/stage_two.git
```

2. Navigate to the project directory:

```
cd my-django-api
```

3. Install the dependencies:

```
pip install -r requirements.txt
```

4. Configure environment variables by creating a .env file in the root directory with the following content:

```
SECRET_KEY=your_secret_key
DB_NAME=database_name
DB_USER=database_user
DB_PASSWORD=database_password
DB_HOST=database_host
```

5. Start the server:

```
python manage.py runserver
```

The API should now be running on http://localhost:8000.

## Usage

### Endpoints

#### Create a New Person

- **Endpoint:** POST /api
- **Description:** Create a new person.

#### Fetch Details of a Person

- **Endpoint:** GET /api/:name
- **Description:** Fetch details of a person by their name or ID.


#### Update the details of an Existing Person

- **Endpoint:** PUT /api/:id
- **Description:** Update details of an existing person by their ID.


#### Delete a Person

- **Endpoint:** DELETE /api/:id
- **Description:** Remove a person by their ID.


### Request Formats

- All request data must be sent in JSON format.
- Include the required fields in the request body.

### Response Formats

- All responses are in JSON format.
- Successful responses return a JSON data
- Error responses have a designated error response


## Demo

The API is live at [https://stage-two-d2n3.onrender.com/api](https://stage-two-d2n3.onrender.com/api)

API documentation with examples [here](https://documenter.getpostman.com/view/23522029/2s9YC4VCwy)

- Author: Adebiyi Oluwafemi
