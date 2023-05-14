default:
  just --list

build *args:
  docker compose build {{args}}

up:
  docker compose up -d

kill *args:
  docker compose kill {{args}}

ps:
  docker compose ps

django *args:
  docker compose exec django python manage.py {{args}}

startapp *args:
  docker compose exec django python manage.py startapp {{args}}

mm *args:
  docker compose exec django python manage.py makemigrations {{args}}

migrate *args:
  docker compose exec django python manage.py migrate {{args}}

ruff *args:
  docker compose exec django ruff src {{args}}

black:
  docker compose exec django black src

lint:
  just black
  just ruff --fix