# Telegram Bot Project

This is a Telegram bot built using **Django** for managing database migrations and the admin panel, and **python-telegram-bot** for handling bot logic. The project is containerized using Docker, with separate `docker-compose` files for development and production environments.

---

## Prerequisites

Before running the bot, ensure you have the following installed:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

---

## Running the Bot

### Development Environment

To run the bot in a development environment:

1. **Copy and fill in the `.env` file.**:
```bash
cp .env.template .env
```

2. **Prepare development environment**:

Run the following command to prepare the development environment:
```bash
uv lock
uv sync --frozen --no-default-groups --only-group dev
ruff format src
ruff check src --preview --fix
```

3. **Build and Start Containers**:

Run the following command to build and start the development environment:
```bash
docker compose -f docker-compose.dev.yml up -d --build
```

4. **Run migration**:

Run the following command to run migrations:
```bash
docker exec {{cookiecutter.project_slug}}-app-dev python manage.py migrate
```

5. **Access the Admin Panel**:

Create superuser:
```bash
docker exec -it {{cookiecutter.project_slug}}-app-dev python manage.py createsuperuser
```
The Django admin panel will be available at http://localhost:{{cookiecutter.open_port}}/admin/

6. **Access the Admin Panel**:

To stop the development environment, run:
```bash
docker compose -f docker-compose.dev.yml down
```

### Production Environment
1. **Create database and user in pg**:
```bash
create user <user_name> with password '<password>';
create database <database_name> owner <user_name>;
```

2. **Copy and fill in the `.env` file.**:
```bash
cp .env.template .env
```

3. **Build and Start Containers**:

Run the following command to build and start the production environment:
```bash
docker compose up -d --build
```

4. **Set up your frontend nginx (Optional)**:

Configure your frontend Nginx to proxy requests to the bot, like:
```nginx configuration
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:{{cookiecutter.open_port}};
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

5. **Updating the Code**:

To update the code and rebuild the containers:
```bash
git pull origin master
docker compose up -d --build
```