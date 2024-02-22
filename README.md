# Django Rating API

The project is a Django-based web application that allows users to list and view content. Each user can rate each piece of content only once.

## Features

- **Content Listing**: Users can view a list of available content.
- **User Ratings**: Each user can rate each piece of content, with a restriction to only one rating per user.

## Installation

To run the project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/armanexplorer/django-rating.git`
2. Create a virtual environment: `python -m venv env`
3. Activate the virtual environment:
   - On Windows: `env\Scripts\activate`
   - On macOS and Linux: `source env/bin/activate`
4. Install the project dependencies: `pip install -r requirements.txt`
5. Apply database migrations: `python manage.py migrate`
6. Start the development server: `python manage.py runserver`
7. You can check the API docs on `/swagger` or `/redoc`

## Usage

1. Access the application by navigating to [http://localhost:8000](http://localhost:8000) in your web browser.
2. Browse the list of available content.
3. If logged in, users can rate the content. The system will ensure that users can only submit one rating per piece of content.

## Technologies Used

- Django
- Python
- PostgreSQL
- gunicorn
- docker
