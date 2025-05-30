DB_CONTAINER=bookshop-postgres-db

start-db:
	docker run --name $(DB_CONTAINER) -p 5432:5432 -e POSTGRES_PASSWORD=postgres postgres

restart-db:
	docker restart $(DB_CONTAINER)

log-db:
	docker container logs $(DB_CONTAINER)

stop-db:
	docker stop $(DB_CONTAINER)

connect-db:
	psql -h localhost -U postgres -d bookshop

clean-db:
	uv run python manage.py flush

clean-containers:
	docker container rm -f $(DB_CONTAINER)

create-migrations:
	uv run python manage.py makemigrations

migrate:
	uv run python manage.py migrate

test:
	uv run python manage.py test -v 2

run:
	uv run python manage.py runserver

console:
	uv run python manage.py shell

populate-db:
	uv run python manage.py runscript populate_db
