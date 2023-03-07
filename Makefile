.DEFAULT_GOAL := help

# ----------------------------
#          COMMANDS
# ----------------------------

.PHONY: help
help: ## Display list of available commands
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: setenv
setenv: ## Create and fill .env file for development
	@echo "DEBUG=True" > devtools/.env
	@echo "POSTGRES_DB="nouvelles_exnihil"" >> devtools/.env
	@echo "POSTGRES_PASSWORD='$(shell tr -dc A-Za-z0-9 </dev/urandom | head -c 26 ;)'" >> devtools/.env
	@echo "PGPORT=5432" >> devtools/.env
	@echo "POSTGRES_USER='nouvelles'" >> devtools/.env
	@echo "POSTGRES_HOST='db'" >> devtools/.env
	@echo "DJANGO_SECRET_KEY='$(shell tr -dc A-Za-z0-9 </dev/urandom | head -c 69 ;)'" >> devtools/.env
	@echo "ALLOWED_HOSTS='0.0.0.0,localhost'" >> devtools/.env

.PHONY: start
start: ## Launch project with postgres database, migration and django web server
	@docker-compose -f devtools/docker-compose.yml up -d

.PHONY: build
build: ## Build project with postgres database, migration and django web server
	@docker-compose -f devtools/docker-compose.yml up --build

.PHONY: css-watch
css-watch: ## Compile scss files with watch mode 
	yarn --cwd style install
	yarn --cwd style start

.PHONY: css-build
css-build: ## Compile scss files
	yarn --cwd style install
	yarn --cwd style css-build

.PHONY: collectstatic
collectstatic: ## Launch collectstatic command in the docker web container and copy static folder on the host machine 
	make start
	@docker exec -it devtools_web_1 python manage.py collectstatic --noinput --clear
	@docker cp devtools_web_1:/app/static/. ./static

.PHONY: seed-local-db
seed-local-db: ## Fill the container db with test data - admin user: admin-admin
	@docker-compose -f devtools/docker-compose.yml up -d db 
	docker exec -i devtools_db_1 /bin/bash -c "psql --username='nouvelles' nouvelles_exnihil" < devtools/dump.sql

.PHONY: clean
clean: ## Remove all docker images related to the project
	@docker images | grep $(DOCKER_IMAGE) | tr -s ' ' | cut -d ' ' -f 2 | xargs -I {} docker rmi $(CI_REGISTRY_IMAGE):{}                                                                                                                                                                                                81,1-8        Bas

