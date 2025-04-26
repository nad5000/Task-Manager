DOCKER_COMPOSE=docker-compose
TEST_DIR=tests/integration_tests

integration-test: up wait-db run-tests down

up:
	$(DOCKER_COMPOSE) up -d --build

run-tests:
	venv/bin/python -m pytest $(TEST_DIR)

down:
	$(DOCKER_COMPOSE) down --volumes

wait-db:
	@echo "Waiting for db_1 to be ready..."
	@until docker exec db_1 psql -U postgres -d postgres -c "SELECT 1;" >/dev/null 2>&1; do \
		echo "Still waiting for db_1..."; sleep 1; \
	done
	@echo "db_1 is ready!"

	@echo "Waiting for db_2 to be ready..."
	@until docker exec db_2 psql -U postgres -d postgres -c "SELECT 1;" >/dev/null 2>&1; do \
		echo "Still waiting for db_2..."; sleep 1; \
	done
	@echo "db_2 is ready!"
	sleep 5

#wait 5 seconds after creation to finish containers setup