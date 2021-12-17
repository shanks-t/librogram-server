## Table of contents
* [Librogram](#Librogram)
* [Features](#features)
* [Tech Stack](#tech-stack)
* [Run Locally](#run-locally)

# Librogram

This is the final, server-side project for NSS full-stack boot camp. The live app is here https://librogram-shanks.herokuapp.com/


## Features

- Full crud functionality with server
- Custom actions for signing up and leaving events
- Custom properties for dynamic event and user content
- Database filtering of events based on queries

## Librogam ERD
https://drawsql.app/nss-7/diagrams/librogram#


## Tech Stack

**Client:** React, HTML, CSS, React-Bootstrap
- https://github.com/DArmstrong87/Librogram

**Server:** Python, Django, SQLite3
- https://github.com/DArmstrong87/Librogram-server
## Run Locally

Clone the project

```bash
  git clone https://github.com/DArmstrong87/Librogram-server
```

Go to the project directory

```bash
  cd Librogram-server
```

Install Pipenv
```bash
curl https://raw.githubusercontent.com/pypa/pipenv/master/get-pipenv.py | python
```

Install dependencies

```bash
  pipenv install django autopep8 pylint djangorestframework django-cors-headers pylint-django
```

Create and initialize a new virtual environment

```bash
  pipenv shell
```

Start server
```bash
  pipenv runserver
```
