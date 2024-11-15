# Anime CRUD App

This is a Python Flask-based web application that provides a CRUD (Create, Read, Update, Delete) interface for managing an anime database. The application handles data for users, anime, and manga. It is deployed in Docker alongside a MySQL database, with a Jenkins pipeline set up to redeploy the container using webhooks.

## Features
- **User Management**: Create, update, and delete user profiles.
- **Anime Database**: Store and manage information about various anime titles.
- **Manga Database**: Manage data for manga series related to anime.

## Technologies Used
- **Python**: Flask framework for the web application.
- **MySQL**: Database to store users, anime, and manga information.
- **Docker**: Containerization of the application and MySQL database.
- **Jenkins**: CI/CD pipeline for automating redeployments using webhooks.

## Getting Started

### Prerequisites
Make sure you have the following installed:
- Docker
- Docker Compose
- Jenkins (for CI/CD pipeline)

### Running the Application Locally

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/your-username/anime-crud-app.git
    cd anime-crud-app
    ```

2. Build and start the application and database using Docker Compose:
    ```bash
    docker-compose up --build
    ```

3. The application will be running on [http://localhost:5000](http://localhost:5000). You can access the CRUD endpoints from here.

### Jenkins Pipeline Setup

1. Set up a Jenkins pipeline that listens to GitHub webhooks to trigger a build and deployment.
2. Configure your Jenkins pipeline with the necessary steps to:
    - Build the Docker container.
    - Deploy the container to your Docker environment.
    - Ensure the database persists across deployments.

### Notes
- The MySQL database is running in a separate container and persists its data unless volumes are removed.
- Ensure your Docker setup retains volumes when deploying to avoid data loss.

## License
This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.
