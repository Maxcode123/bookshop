run:
	docker-compose up -d database backend

restart:
	docker-compose restart database backend

build-dev:
	DOCKER_BUILDKIT=1 docker-compose build --build-arg BUILD_GROUPS="--group dev" backend

build-prod:
	DOCKER_BUILDKIT=1 docker-compose build backend

stop:
	docker-compose down

log:
	docker-compose logs backend

log-db:
	docker-compose logs database

connect-db:
	psql -h localhost -p 5432 -U postgres -d bookshop

clean-db:
	uv run python manage.py flush

create-migrations:
	uv run python manage.py makemigrations

migrate:
	uv run python manage.py migrate

test:
	docker-compose up -d --no-deps database
	docker-compose run backend python manage.py test -v 2
	docker-compose down

console:
	uv run python manage.py shell

format:
	ruff format ./

populate-db:
	uv run python manage.py runscript populate_db
