VENVDIR=venv
BINDIR=$(VENVDIR)/bin

# Create the virtual environment and activate it
venv:
	python -m venv $(VENVDIR)
.PHONY: install-deps setup
# Lock the dependencies, then install them
install-deps:
	$(BINDIR)/pip install pip-tools
	$(BINDIR)/pip-compile --output-file requirements.txt requirements.in
	$(BINDIR)/pip-compile --output-file requirements-dev.txt requirements-dev.in
	$(BINDIR)/pip install -r requirements.txt
	$(BINDIR)/pip install -r requirements-dev.txt
activate:
	echo "To activate the virtual environment, run: . $(VENVDIR)/bin/activate"
# Setup the project, create venv, lock & install dependencies
setup: venv install-deps
