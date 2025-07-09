# django-hello-world

A minimal Django starter project to learn the basics of Django.

## Setup and Installation

This project uses a Python virtual environment (`venv`) with Django already installed.

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd django-hello-world
```

### 2. Activate the virtual environment

##### On macOS/Linux:

```
source venv/bin/activate
```

##### On Windows (PowerShell):

```
.\venv\Scripts\Activate.ps1
```

### 3. Verify Django is installed

```
python3 -m django --version
```

You should see the installed Django version.

## Running the Development Server

Start the Django development server:

```
python3 manage.py runserver
```

Visit http://127.0.0.1:8000 in your browser to see the project running.

---

# To-do

- [x] List to-dos
- [x] add to-do details (route navigation)
- [x] add input to create todo
- [x] update to-dos
- [ ] create a base template HTML
- [ ] add scss
- [ ] add unit tests

# Learning

- Django is not an SPA
- WSGI (Web Server Gateway Interface): A Python standard to define comunication between a web server and Python web application
- ASGI (Asynchronous Server Gateway Interface): successor to WSGI. Enable synchronous and asynchronous communication.
- pk (primary key): Example `Todo.objects.get(pk=todo_id). Means "find object by primary key todo id"
