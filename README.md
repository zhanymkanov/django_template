# Django Project Template

This is a Django project template for Django 4.2 that I use to start new projects.
- Docker, docker-compose
- Pydantic for configs loading
- Configured with uvicorn for async compatibility
- [just](https://github.com/casey/just) for shortcuts
- black + ruff for linting
- Simple logging

### How to start working
Prerequisites:
- Install [just](https://github.com/casey/just)
- Install docker

1. Build the project
```shell
just build
```
2. Run the project
```shell
just up
```
3. Migrate the database
```shell
just migrate
```
4. Create superuser
```shell
just django createsuperuser
```
5. Collect static
```shell
just django collectstatic
```
6. Done! Go to http://0.0.0.0:8100/admin/ and login with the superuser you created.

### Shortcuts
- `just` - list all available shortcuts

Docker shortcuts:
- `just build` - build the project
- `just up` - run the project

Linting shortcuts:
- `just lint` - lint the project with black and ruff
- `just black` - just black the project
- `just ruff` - just ruff the project

Django shortcuts:
- `just migrate` - migrate the database
- `just mm *app_name* -n *migration_name*` - create a migration for the _app_name_ called _migration_name_
- `just django` - run django management command
- `just startapp *app_name*` - create a new app called _app_name_
