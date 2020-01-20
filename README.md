# drf-articles

Simple REST API, using Django & Django REST Framework.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.7 or later

### Installing

1. Clone the repository to your local machine:

   `git clone https://github.com/Hephest/drf-articles.git`

2. Create virtual environment via `venv`:

   `python -m venv venv/`

3. Activate development environment, depending on your computer OS:

   * **Windows:** `venv/Scripts/activate.bat`
   * **Linux:** `source  venv/bin/activate`

4. Install neccessary packages, using information from `requirements.txt`:

   `pip install -r requirements.txt`

## Running the tests

Runnning tests by Django test runner: `./manage.py test`

## Built With

* [Django](https://www.djangoproject.com/) - Python web framework used
* [Django REST Framework](https://www.django-rest-framework.org/) - Powerful and flexible toolkit for building Web APIs
* [Swagger](https://swagger.io/) - Open-source software framework backed by a large ecosystem of tools that helps developers design, build, document, and consume RESTful web services.

## Status

### 1/20/20

**Total:** 0:25 h

* Added `requirements.txt`
* Updated `README.md`

### 1/6/20

**Total:** 3:05 h

* Each user could see and edit their own article
* Filter option for `articles/` list
* Updated data render for `article/stats/` endpoint
* Tests
    * `test_models`
    * `test_views`

### 1/4/20

**Total:** 1:15 h

* Basic REST API setup
* `docs/` - Swagger documentation
* `article/stats/` - Custom endpoint for objects stats
    * JSON renderer
    * Count of total articles