# YourRecipiesHolder 

A simple Django-based web application demonstrating full Create, Read, Update, and Delete (CRUD) operations on a sample model using Python, Django, HTML, CSS, and JavaScript.

## Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Database Migrations](#database-migrations)
- [Running the Development Server](#running-the-development-server)
- [CRUD Functionality](#crud-functionality)
- [URLs and Views](#urls-and-views)
- [Templates and Static Files](#templates-and-static-files)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project showcases a basic Django application that performs standard CRUD operations on a sample model (e.g., `Item`). Users can:

- **Create** new records via a form
- **Read** (list and detail) existing records
- **Update** records through an editable form
- **Delete** records with confirmation

All operations are handled via Django views, forms, and templates, with minimal JavaScript enhancements for improved UX.

## Tech Stack

- **Backend**: Python 3.x, Django 4.x
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (default)

## Prerequisites

- Python 3.8 or higher installed
- `pip` package installer
- (Optional) `virtualenv` or `venv` for isolated environments

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/otAdarshP/Django_CRUD_Operations.git
   cd Django_CRUD_Operations
   ```
2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install django
   ```

*(If a `requirements.txt` file is provided, run `pip install -r requirements.txt` instead.)*

## Project Structure

```bash
Django_CRUD_Operations/
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies (if available)
├── Django_CRUD_Operations/  # Project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Root URL conf
│   └── wsgi.py             # WSGI entrypoint
├── myapp/                  # Main application
│   ├── migrations/         # Database migrations
│   ├── admin.py            # Admin registrations
│   ├── apps.py             # App configuration
│   ├── models.py           # Data model definitions
│   ├── forms.py            # Django forms for CRUD
│   ├── views.py            # CRUD views (list, detail, create, update, delete)
│   ├── urls.py             # App-specific URLs
│   ├── templates/          # HTML templates
│   │   └── myapp/          # Template directory
│   │       ├── base.html
│   │       ├── item_list.html
│   │       ├── item_detail.html
│   │       ├── item_form.html
│   │       └── item_confirm_delete.html
│   └── static/             # Static assets (CSS, JS)
│       └── myapp/
│           ├── css/
│           └── js/
└── db.sqlite3              # SQLite database (auto-generated)
```

## Database Migrations

After installation, generate and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Running the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to access the application.

## CRUD Functionality

- **List View**: Displays all `Item` records with links to view, edit, or delete.
- **Detail View**: Shows full details of a single record.
- **Create View**: Presents a form to add a new record.
- **Update View**: Pre-populates a form to edit an existing record.
- **Delete View**: Asks for confirmation before removing a record.

## URLs and Views

| URL Pattern               | View Name            | Purpose                      |
| ------------------------- | -------------------- | ---------------------------- |
| `/items/`                 | `item_list`          | List all items               |
| `/items/<int:pk>/`        | `item_detail`        | View item details            |
| `/items/create/`          | `item_create`        | Add a new item               |
| `/items/<int:pk>/edit/`   | `item_update`        | Edit an existing item        |
| `/items/<int:pk>/delete/` | `item_delete`        | Delete an existing item      |

*(Adjust `urls.py` if you have a different app or URL scheme.)*

## Templates and Static Files

- **Templates** are located in `myapp/templates/myapp/`.
- **Static files** (CSS/JS) live under `myapp/static/myapp/`.
- Base layout (`base.html`) includes common header, navigation, and static file references.

## Customization

- **Model Changes**: Edit `models.py` to add fields; run `makemigrations` and `migrate`.
- **Form Adjustments**: Update or extend `forms.py` for custom validation.
- **Styling**: Modify CSS under `static/myapp/css/`.
- **URLs**: Add or remove routes in `myapp/urls.py` and corresponding views.

## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m "Add YourFeature"`.
4. Push to your fork: `git push origin feature/YourFeature`.
5. Open a Pull Request.

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.

