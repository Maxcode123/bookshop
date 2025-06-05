# bookshop

A Django backend for a bookstore application.

## API

### GET /books/  
List all books  
Available query parameters:  
**genre**  
genre uuid; list books that belong to the given genre or any of its' descendants.  
**author**  
author uuid; list books that belong to the given author.  
**publisher**  
publisher uuid; list books of the given publisher.  

### GET /books/<uuid>  
Show details of a book  

### GET /genres/  
List all genres  

### GET /authors/  
List all authors  

### GET /publishers/  
List all publishers  

## Development

List of available commands:

**make start-db**: start the postgres database in a docker container; this command uses a predefined name for the docker container, thus you cannot execute this command if a container already exists with that name; use `make restart-db` for that  
**make restart-db**: restart the docker container running the postgres database. Use this command to start the same container each time, e.g. if you want to keep your data every time you use the app  
**make log-db**: output the logs of the database container in standard output  
**make stop-db**: stop the database container  
**make connect-db**: connect to the database container using `psql` as a client  
**make clean-db**: remove all the data from your database  
**make populate-db**: populate the database with seed data  
**make clean-containers**: delete the database container; you will have to run `make start-db` the next time you want to start the database  
**make create-migrations**: use django to create a migration file based on your local changes  
**make migrate**: apply pending migrations  
**make run**: run the application server, accessible on http://localhost:8000  
**make console**: open a django shell  
**make format**: format all files with ruff  

## Dependencies

- django-extensions
- django-ltree
- djangorestframework
- psycopg2
