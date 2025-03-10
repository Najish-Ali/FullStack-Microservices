**Project: Multi-Service Application with API Gateway, UI, and API**
====================================================================

This project is a multi-service application that includes:

-   **API Gateway**: Built with FastAPI, handles user registration, pipeline triggering, and rollback.

-   **UI Application**: Built with Node.js and Express, provides a user interface for registration.

-   **API Application**: Built with Node.js and Express, serves as a backend service.

-   **PostgreSQL Database**: Used for storing user information and schema data.

The application is containerized using Docker and can be deployed locally or on a cloud platform.

**Features**
------------

-   **User Registration**: Users can register via the UI, and a new schema is created in the database.

-   **Pipeline Automation**: Trigger CI/CD pipelines for UI, API, and database services.

-   **Rollback Mechanism**: Rollback changes in case of pipeline failures.

-   **Containerized Services**: All services are Dockerized for easy deployment.

-   **CI/CD Integration**: GitHub Actions workflows for automated testing and deployment.

* * * * *

**Prerequisites**
-----------------

Before running the project, ensure you have the following installed:

-   [Docker](https://docs.docker.com/get-docker/)

-   [Docker Compose](https://docs.docker.com/compose/install/)

-   [Node.js](https://nodejs.org/) (v16 or higher)

-   [Python](https://www.python.org/) (v3.9 or higher)

-   [PostgreSQL](https://www.postgresql.org/) (or access to an AWS RDS PostgreSQL instance)

-
