.PHONY: help % test cc ci linting mypy ruff formatting black ruff-fix clean create-environment install-dependencies install-pre-commit-hooks install
.DEFAULT_GOAL := help

# Virtual environment paths
VIRTUAL_ENV_NAME := .venv
TOOLS_FIRST_INSTALLED := $(VIRTUAL_ENV_NAME)/.tools_first_installed

# Directories
ROOT_DIR := $(CURDIR)
BIN_DIR := $(ROOT_DIR)/bin
PKG_DIR := $(ROOT_DIR)/src
TEST_DIR := $(ROOT_DIR)/tests

help:
	@$(BIN_DIR)/help.sh "$(MAKEFILE_LIST)"

%:
	@echo "Target $@ is not defined. Running help target instead:\n"
	@$(MAKE) help

test: ## Run test suite
	@poetry run pytest $(TEST_DIR) --suppress-no-test-exit-code

cc: ## Compute cyclomatic complexity of source code
	@radon cc -ase "**/__init__.py" src

ci: linting test ## Emulate CI pipeline (linters and tests)

linting: ruff mypy ## Run all linters

ruff:
	@poetry run ruff check $(PKG_DIR)

mypy:
	@poetry run mypy $(PKG_DIR)

formatting: black ruff-fix ## Run all formatters

black:
	@poetry run black $(PKG_DIR) $(TEST_DIR)

ruff-fix:
	@poetry run ruff check --fix $(PKG_DIR) $(TEST_DIR)

clean: ## Clean all temporary folder/files on the project
	@rm -rf $(ROOT_DIR)/.cache

install: create-environment $(TOOLS_FIRST_INSTALLED) install-dependencies install-pre-commit-hooks ## Setup environment and install all dependencies

$(TOOLS_FIRST_INSTALLED):
	@touch $@

create-environment:
	@pyenv install --skip-existing $(shell cat $(ROOT_DIR)/.python-version)
	@poetry env use -- $(shell pyenv which python)

install-dependencies:
	@poetry install --with dev,test

install-pre-commit-hooks: $(TOOLS_FIRST_INSTALLED)_hooks
$(TOOLS_FIRST_INSTALLED)_hooks:
	@poetry run pre-commit install
	@touch $@
