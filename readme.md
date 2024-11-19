
# Project Overview

This is a Django-based backend API project. It is built using Django 5.x, Django REST Framework, and PostgreSQL. The project uses Docker to manage the backend and database containers.

## Quick Start Guide

### 1. Clone the repository

```bash
git clone https://github.com/y00tss/AdSt
cd AdSt
```

### 2. Run the project with Docker Compose

To build and run the application:

```bash
docker-compose up --build
```

### 3. Access the API

- **Backend API**: `http://localhost:8001/`
- **Swagger UI (DRF Spectacular)**: `http://localhost:8001/api/schema/swagger-ui/`

### 4. Stopping the Application

To stop the containers:

```bash
docker-compose down or CTRL + C
```

---
