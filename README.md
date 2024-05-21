# Sticky Notes Task Manager

## Description

Sticky Notes Task Manager is a Django-based web application that allows users to create, read, update, and delete notes. This project is designed to help users manage their tasks efficiently.

## Table of Contents
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Steps](#steps)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Credits](#credits)

## Installation

To run this Django project locally, follow these steps:

### Prerequisites

- [Python](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (optional but recommended)

### Steps

1. **Clone the repository**:
    ```sh
    git clone https://github.com/tu-usuario/codingTasks.git
    cd codingTasks/sticky_notes
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```sh
    python -m venv env
    # On Windows
    .\env\Scripts\activate
    # On MacOS/Linux
    source env/bin/activate
    ```

3. **Install project dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure the database**:
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser** (optional):
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

Visit `http://127.0.0.1:8000/` in your browser to see the application running.

## Usage

After installing the project, you can perform the following actions:

- **Create a new note**: Click on create a new note and fill out the form to create a new sticky note.
- **Read existing notes**: The home page lists all the sticky notes.
- **Update a note**: Click on a note title to edit its content.
- **Delete a note**: Click the delete button next to a note to remove it.

## Credits

Developed by Pedro Pablo Sanchez Lopez.
