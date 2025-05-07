DB_CONTAINER=bookshop-postgres-db

start-db:
	docker run --name $(DB_CONTAINER) -p 5432:5432 -e POSTGRES_PASSWORD=postgres postgres

restart-db:
	docker restart $(DB_CONTAINER)
	docker container logs --follow $(DB_CONTAINER)

stop-db:
	docker stop $(DB_CONTAINER)

connect-db:
	psql -h localhost -U postgres -d bookshop

clean-containers:
	docker container rm -f $(DB_CONTAINER)

test:
	python manage.py test -v 2

run:
	python manage.py runserver
