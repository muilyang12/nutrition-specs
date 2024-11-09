# Nutrition Specs

Nutrition Specs is a web service for comparing nutritional information across multiple products within the same category, helping users make informed dietary choices.

## Technologies Used

### Backend

- Python
- Django
- Django REST Framework
- SQLite3

### Frontend

- TypeScript
- Next.js
- Zustand for state management

### Deployment

- Docker for containerization
- AWS Services:
  - S3: Storage for static files
  - EC2: Server hosting
  - CloudFront: CDN for faster delivery
  - Route 53: Domain name management
  - ECR: for storing Docker images

## Prerequisites

- Python
- Node.js
- Docker
- AWS CLI

## Setup

### 1. Clone the Repository

### 2. Backend Setup

- Change to the Project Directory

  ```
  cd be
  ```

- Create a Virtual Environment

  ```
  python -m venv .venv
  ```

- Install Dependencies

  ```
  pip install -r requirements.txt
  ```

- Apply Database Migrations and Run the Application

  ```
  python manage.py migrate
  python manage.py runserver
  ```

### 3. Frontend Setup

- Change to the Frontend Directory

  ```
  cd fe
  ```

- Install Dependencies

  ```
   npm install
  ```

- Run the Development Server

  ```
   npm run dev
  ```
