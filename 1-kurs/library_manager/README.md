# Library Manager

A Django-based library management system.

## prerequisites

- Python 3.10 or higher
- pip (Python package manager)

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd library_manager
    ```

2.  **Create and activate a virtual environment (optional but recommended):**

    ```bash
    # Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

6.  **(Optional) Load initial data:**
    
    This script creates a superuser (`admin`/`admin123`), a test user (`student`/`student123`), and sample books.
    ```bash
    python setup_data.py
    ```

## Running the Application

1.  **Start the development server:**

    ```bash
    python manage.py runserver
    ```

2.  **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000/`.

    To access the admin panel, go to `http://127.0.0.1:8000/admin/`.

    **Default Credentials (if setup_data.py was run):**
    - Admin: `admin` / `admin123`
    - Student: `student` / `student123`
