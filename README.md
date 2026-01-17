# Student Management System

A simple web-based Student Management System built with Flask.

## Features

- **Dashboard**: View all students in a table format.
- **Search**: Filter students by name or class using the search bar.
- **Add Student**: Form to add new students with personal details and grades.
- **Edit Student**: specific functionality to edit student details.
- **Delete Student**: specific functionality to remove a student.
- **Student Details**: View detailed information about a specific student.
- **Statistics**: View class average, top student, and subject-wise performance.

## Setup

1.  **Prerequisites**: Python 3.x installed.
2.  **Installation**:
    ```bash
    pip install flask
    ```
3.  **Run the Application**:
    ```bash
    python3 app.py
    ```
4.  **Access**: Open your browser and navigate to `http://127.0.0.1:5000`.

## Project Structure

- `app.py`: Main Flask application file defining routes and logic.
- `models.py`: Contains the `Student` and `StudentManager` classes for data handling.
- `templates/`: HTML templates for the application pages.
- `static/`:  Static files like CSS.
