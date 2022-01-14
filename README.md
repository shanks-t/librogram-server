## Overview
I love books, have since I was very small. They have been a source of comfort and exploration for me all my life. This app is an expression of my joy for reading. It allows users to search for books via google's free books api, and then save all the books they've ever read to their user library. Users can make comments about the books in their library and see coments from other users who have checked out the same book. Also, in the user profile users can set reading goals which are dynamically updated as they update the progress of each book by setting the status of the book to 'unread', 'in-progress' or 'finished'. Users can also filter their personal library by category, rating, or number of pages, as well as search for books by typing the title in the user library serach bar. Once logged in, simply search for books and click the ones you'd like to add. Then edit details of each book by clicking on the book. Use the navbar 'actions' dropdown to set reading goals and update the user bio. 


## Table of contents
* [Librogram](#Librogram)
* [Features](#features)
* [Tech Stack](#tech-stack)
* [Run Locally](#run-locally)

# Librogram

This is the final, server-side project for NSS full-stack boot camp. The live app is here https://librogram-shanks.herokuapp.com/


## Features

- Full crud functionality with server
- Filtering books by title, author, book length or category via django ORM
- A custom property for calculating and updating progress toward reading goals

## Librogam ERD
https://drawsql.app/nss-7/diagrams/librogram#


## Tech Stack

**Client:** ReactJS, HTML, CSS, React-Bootstrap
- https://github.com/shanks-t/librogram-client

**Server:** Python, Django, SQLite3
- https://github.com/shanks-t/librogram-server
## Run Locally

Clone the project

```bash
  git clone https://github.com/shanks-t/librogram-server
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
<<<<<<< HEAD
Clone Frontend Repo Listed above 
```bash
  git clone https://github.com/shanks-t/librogram-server
```
Run the React app  
```bash
  npm start
```
=======
>>>>>>> main
