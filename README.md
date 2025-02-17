# Media Platform API
This project implements a backend API for managing hierarchical media content using Django.
The API organizes media content into channels, supports hierarchical relationships, calculates
ratings dynamically, and exports data to a CSV file.

We need to define an API for our media platform that organizes content in a hierarchical structure.
Each piece of content can include files (e.g., videos, PDFs, or text), metadata (such as descriptions,
authors, and genres), and a rating between 0 and 10.

Content is managed through Channels, which define the hierarchy. A channel has a title, language,
and image, and it can either contain subchannels or content, but never both. Each channel must have at
least one subchannel or one content item.

A channel's rating is calculated dynamically as the average rating of its subchannels or, if it has
none, the average of its contents. Channels without content do not contribute to their parent's rating.
Since the structure is dynamic, ratings cannot be stored directly and must be computed as needed.

## Index
* [Features](#features)
* [Requirements](#requirements)
* [Installation](#installation)
* [Data Model](media_platform/TABLE_MODEL.md)
* [Usage](#usage)
* [Admin Management](#admin-management)
* [Testing](#testing)
* [Docker setup](#docker-setup)
* [Folder Structure](#folder-structure)
* [Future Improvements](#future-improvements)
* [License](#license)

## Features
- Manage hierarchical channels and their associated content.
- Compute dynamic ratings for channels based on their contents or subchannels.
- Filter channels by groups.
- Export channel ratings to a CSV file.
- RESTful API endpoints for managing channels, contents, and groups.
- Built-in unit tests to validate functionality.
- Optional Docker environment for easy deployment.

## Requirements
- Python 3.9 or later
- Django 4.x
- Django REST Framework (DRF)
- PostgreSQL (recommended) or SQLite
- Docker (optional, for containerized deployment)

## Installation
### Step 1: Clone the Repository
```bash
git clone git@github.com:manel.jimeno/media_django_sample.git
cd media_django_sample
```

### Step 2: Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Run the Server
```bash
python manage.py runserver
```
The API will be accessible at http://127.0.0.1:8000.

## Usage
### Endpoints
- Channels:
  - `GET /api/channels/`: List all channels.
  - `GET /api/channels/?group=<group_id>`: Filter channels by group.
  - `POST /api/channels/`: Create a new channel.
  - `GET /api/channels/<id>/`: Retrieve details of a specific channel.
- Contents:
  - `GET /api/contents/`: List all contents.
  - `POST /api/contents/`: Create new content.
- Groups:
  - `GET /api/groups/`: List all groups.
  - `POST /api/groups/`: Create a new group.

### Export Ratings
Run the management command to export channel ratings to a CSV file:

```bash
python manage.py export_channel_ratings
```
This will generate a file named `channel_ratings.csv` with two columns: `Channel Title` and `Average Rating`.

## Admin Management
### Create an Admin User
To manage the `Content`, `Channel`, and `Group` models through the Django admin interface, you first need to create
an admin user:
```bash
python manage.py createsuperuse
```
Provide the required information:
- Username: The admin username.
- Email address: The admin email (optional).
- Password: A secure password for the admin account.

Once created, log in to the Django admin panel at:
```bash
http://127.0.0.1:8000/admin
```

### Managing Tables in Admin
The following models can be managed from the admin panel:

1. Content:
   - Add or edit individual pieces of media content.
   - Configure metadata, file URLs, and ratings.
2. Channel:
   - Create or edit channels, including hierarchical relationships.
   - Assign subchannels or associate content with a channel.
   - Group channels by using the Group feature.
3. Group:
   - Add or manage channel groups.
   - Use groups to filter channels through the API.

### Admin Features
The admin interface provides:

- Search functionality for quickly finding specific records.
- List filters for filtering by attributes (e.g., ratings, language, or groups).
- Inline editing for managing related models (e.g., linking Contents to a Channel).

## Testing
To run unit tests:

```bash
python manage.py test
```

## Docker Setup
To run the project in a Docker container:

 1. Build the Docker image:
    ```bash
    docker-compose build
    ```
 2. Run the container:
    ```bash
    docker-compose up
    ```

The API will be available at http://localhost:8000.

## Folder Structure
```bash
media/
│
├── media_platform/
│   ├── migrations/          # Database migrations
│   ├── models.py            # Database models
│   ├── serializers.py       # API serializers
│   ├── views.py             # API views
│   ├── urls.py              # App-specific URLs
│   ├── tests.py             # Unit tests
│   ├── management/
│       ├── commands/
│           ├── export_channel_ratings.py  # CSV export command
│
├── media/
│   ├── settings.py          # Project settings
│   ├── urls.py              # Root URLs
│   ├── asgi.py              # Application definition (Daphne, Uvicorn)
│   ├── wsgi.py              # Application definition (Gunicorn, uWSGI, mod_wsgi)
│
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose configuration
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
```

## Future Improvements
- Add user authentication and permissions for managing channels and contents.
- Implement caching for performance optimization in rating calculations.
- Extend CI/CD pipelines for automated testing and deployment.

## License
This project is developed as part of a technical demonstration and is not intended for production use.
