# Makefile

# Python interpreter to use
PYTHON := python3

# Script to run
SCRIPT := feature_extraction.py

# Define phony targets (targets that don't represent files)
.PHONY: check black isort flake8 mypy pylint run

# Default target
all: check

# Run all checks
check: black isort flake8 mypy pylint

# Run black
black:
	@echo "Running Black..."
	$(PYTHON) -m black .

# Run isort
isort:
	@echo "Running isort..."
	$(PYTHON) -m isort .

# Run flake8
flake8:
	@echo "Running flake8..."
	$(PYTHON) -m flake8 .

# Run mypy
mypy:
	@echo "Running mypy..."
	$(PYTHON) -m mypy .

# Run pylint
pylint:
	@echo "Running pylint..."
	$(PYTHON) -m pylint **/*.py

# Run the script
run:
	@echo "Running $(SCRIPT)..."
	$(PYTHON) $(SCRIPT)

# Clean up Python cache files
clean:
	@echo "Cleaning up Python cache files..."
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

# Help target
help:
	@echo "Available targets:"
	@echo "  check   : Run all linting tools"
	@echo "  black   : Run Black formatter"
	@echo "  isort   : Run isort import sorter"
	@echo "  flake8  : Run flake8 linter"
	@echo "  mypy    : Run mypy type checker"
	@echo "  pylint  : Run pylint"
	@echo "  run     : Run the Python script"
	@echo "  clean   : Remove Python cache files"
	@echo "  help    : Show this help message"
