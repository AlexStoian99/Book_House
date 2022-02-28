# ==================================================================================================
# Variables
# ==================================================================================================

MODULES:=polls
PACKAGE_NAME=polls
EXECUTABLE_NAME:=polls

PYTHON:=$(shell which python3.9)
PIP:=$(PYTHON) -m pip
PIPENV:=$(PYTHON) -m pipenv
PIPENV_LOCK_ARGS:= --deploy --ignore-pipfile

# ==================================================================================================
# Install targets
# ==================================================================================================

ensure-pipenv:
	$(PIP) install --user --upgrade pipenv pip

pipenv-install-dev:
# Do not use destructive "--python" or "--three" option if the venv already exists
# See https://github.com/pypa/pipenv/issues/349
	@if $(PIPENV) --venv; then \
		echo "$(PIPENV) install --dev $(PIPENV_LOCK_ARGS)"; \
		$(PIPENV) install --dev $(PIPENV_LOCK_ARGS); \
	else \
		echo "$(PIPENV) install --dev $(PIPENV_LOCK_ARGS) --python $(PYTHON)"; \
		$(PIPENV) install --dev $(PIPENV_LOCK_ARGS) --python $(PYTHON); \
	fi

dev: ensure-pipenv pipenv-install-dev  ## Setup dev environment

# ==================================================================================================
# Code formatting targets
# ==================================================================================================

style: isort autopep8 yapf  ## Format code

isort:
	$(PIPENV) run isort $(MODULES)

autopep8:
	$(PIPENV) run autopep8 --in-place --recursive $(MODULES)

#yapf:
#	$(PIPENV) run yapf --recursive --parallel -i $(MODULES)

# ==================================================================================================
# Static checks targets
# ==================================================================================================

checks: isort-check yapf-check flake8 pylint  ## Static analysis

isort-check:
	$(PIPENV) run isort -c $(MODULES)

#yapf-check:
#	$(PIPENV) run yapf --recursive --diff $(MODULES)

flake8:
	$(PIPENV) run flake8 $(MODULES)

pylint:
	$(PIPENV) run pylint $(MODULES)

# ==================================================================================================
# Test targets
# ==================================================================================================

test:  ## Execute unit tests
	$(PIPENV) run pytest $(MODULES)

test-v:  ## Execute verbose unit tests
	$(PIPENV) run pytest -vv $(MODULES)

test-coverage:
	$(PIPENV) run pytest --cov-config=.coveragerc --cov=$(PACKAGE_NAME) --cov-report=html:coverage_html --cov-report=term $(MODULES)

# ==================================================================================================
# Misc targets
# ==================================================================================================

shell:
	$(PIPENV) shell

ctags:
	find -name '*.py' -exec ctags -a {} \;

update: mk-venv pipenv-update pipenv-install-dev  ## Update dependencies

pipenv-update:
	$(PIPENV) update --clear

update-recreate: update style check test

lock:
	$(PIPENV) lock

# ==================================================================================================
# Aliases to gracefully handle typos on poor dev's terminal and provide short forms
# ==================================================================================================

sc: style check
sct: style check test
check: checks
styles: style
tests: test