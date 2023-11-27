# Makefile for Flask Application with Gunicorn

# Set the virtual environment name
VENV_NAME = CS410

# Python interpreter path within the virtual environment
VENV_PYTHON = $(VENV_NAME)/bin/python

# Gunicorn command to run the application
GUNICORN = $(VENV_NAME)/bin/gunicorn

# WSGI entry point for your Flask app
WSGI_APP = wsgi:app

# Target: setup - Create a virtual environment
setup:
	python3 -m venv $(VENV_NAME)

# Target: install - Install project dependencies
install: setup
	$(VENV_PYTHON) -m pip install -r requirements.txt

# Target: run - Run the Flask application with Gunicorn
debug: install
	$(GUNICORN) -c gunicorn.py $(WSGI_APP)

# Target: deploy - Run the Flask application with Gunicorn daemonized and the unified worker
run: install
	$(GUNICORN) -c gunicorn.py $(WSGI_APP) -D
	$(VENV_PYTHON) app/unified_worker.py

# Target: stop - Stop the Flask application daemon
stop:
	pkill -f gun

# Target: clean - Remove the virtual environment
clean:
	rm -rf $(VENV_NAME)

# Target: test - Run tests (if applicable)
test: install
	$(VENV_PYTHON) -m pytest

# Help target: Display available targets
help:
	@echo "Available targets:"
	@echo "  setup       - Create a virtual environment"
	@echo "  install     - Install project dependencies"
	@echo "  run         - Run the Flask application with Gunicorn"
	@echo "  clean       - Remove the virtual environment"
	@echo "  test        - Run tests (if applicable)"
	@echo "  help        - Display this help message"

# Default target: Display available targets
.DEFAULT_GOAL := help
