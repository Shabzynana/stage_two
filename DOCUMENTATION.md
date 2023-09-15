# Project Documentation

This document provides detailed information on how to use the REST API for the "Person" resource.

> LIVE API Endpoint are https://stage-two-d2n3.onrender.com/api
>

Please refer to this documentation for request/response formats, sample API usage.
>
>Link to **POSTMAN** documentation of this api https://documenter.getpostman.com/view/21871844/2s9YC32Zfm
>

## Table of Contents
* [Setup Instructions](#setup-instructions)
* [API Endpoints](#api-endpoints)

---

## Setup Instructions
To setup the api on your local machine, follow this steps on you command terminal

1. **Clone the Repository:**
```
git clone https://github.com/shabzynana/stage_two.git
cd stage_two
```

2. **Setup the Virtual Environment**
create a Virtual environment
```
python -m venv project
```
activate
```
source pro/bin/activate
```

3. **Install Requirements:**
```
pip install -r requirements.txt
```

4. **Run the Server Locally:**
```
python manage.py runserver
```

5. The API will be available locally at `http://localhost:5000`.

---

## API Endpoints

The API provides the following endpoints for CRUD operations on the "Person" resource:

* **[Create](#create-a-person-post-api)**---
    Adding new person [POST]

    * **`/api`**

* **[Read All (List)](#read-all-persons)**---
    Retrieving all persons in database [GET]

    * **`/api`**

* **[Read A Single Person](#read-a-person-by-name)**---
    Retrieving a specific person by name [GET]
    * **`/api/{name}`**


* **[Update A Person](#update-a-person-by-id)**---
    Updating a particular existing person by id [PUT]
    * **`/api/{id}`**

* **[Delete A Person](#delete-a-person-by-id)**---
    Delete a particular existing person by id [DELETE]
    * **`/api/{id}`**
