.PHONY: help install lint test build publish publish-test clean

VENV_ACTIVATE = source .venv/bin/activate
PIP = pip
PYTHON = python

ifeq ($(OS),Windows_NT)
	VENV_ACTIVATE = .venv/Scripts/activate
	PIP = pip
	PYTHON = python
endif

PACKAGE = startling_lib
VERSION = $(shell $(PYTHON) -c "import setuptools; print(setuptools.config.read_configuration('pyproject.toml')['version'])")

help:
	@echo "💡 Available commands:"
	@echo "  make install        → Install dev dependencies (dans .venv)"
	@echo "  make test           → Run tests with coverage"
	@echo "  make lint           → Lint avec flake8"
	@echo "  make build          → Build wheel + sdist"
	@echo "  make publish        → Publier sur PyPI"
	@echo "  make publish-test   → Publier sur TestPyPI"
	@echo "  make clean          → Supprimer fichiers temporaires"

install:
	@echo "📦 Installing in .venv..."
	$(PIP) install -e .[dev]

lint:
	@echo "🔍 Running flake8..."
	$(PYTHON) -m flake8 $(PACKAGE)

test:
	@echo "🧪 Running tests..."
	$(PYTHON) -m pytest --cov=$(PACKAGE) tests/

build:
	@echo "📦 Building distribution..."
	rm -rf dist/ build/ *.egg-info
	$(PYTHON) -m build

publish: build
	@echo "🚀 Publishing to PyPI..."
	$(PYTHON) -m twine upload dist/*

publish-test: build
	@echo "🧪 Publishing to TestPyPI..."
	$(PYTHON) -m twine upload --repository testpypi dist/*

clean:
	@echo "🧹 Cleaning build files..."
	rm -rf dist/ build/ *.egg-info .pytest_cache .mypy_cache .coverage
