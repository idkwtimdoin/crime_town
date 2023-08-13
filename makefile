
PROJECT_PATH := $(shell git rev-parse --show-toplevel)
VENVNAME := .venv
VENVPATH := $(PROJECT_PATH)/$(VENVNAME)/bin

.venv:
	@python3.10 -m virtualenv $(VENVNAME)

install: .venv
	@. .venv/bin/activate
	@$(VENVPATH)/pip3 install --upgrade pip
	@$(VENVPATH)/pip3 install -r requirements.txt

clean:
	rm -rf .venv/

format:

lint:

test:
