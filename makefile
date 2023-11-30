
PROJECT_PATH := $(shell git rev-parse --show-toplevel)
VENVNAME := .venv
VENVPATH := $(PROJECT_PATH)/$(VENVNAME)/bin

SRC_DIR := $(PROJECT_PATH)/src
TEST_DIR := $(PROJECT_PATH)/tests

LINT_MAX_LINE_LENGTH := 120

.venv:
	@python3.10 -m virtualenv $(VENVNAME)

install: .venv
	. $(VENVPATH)/activate && \
		$(VENVPATH)/pip3 install -U pip wheel "setuptools<60" && \
		$(VENVPATH)/pip3 install --upgrade pip  && \
		$(VENVPATH)/pip3 install -r requirements.txt

clean:
	@rm -rf .venv/

rmvol:
	@rm -rf ./db/data || \
		rm -rf ./mysql_db/data || \
		rm -rf ./postgres_db/data || true

format:
	@$(VENVPATH)/pre-commit run trailing-whitespace --all-files || true
	@$(VENVPATH)/pre-commit run end-of-file-fixer --all-files || true
	@echo "-+-+-+-+-+-+-+-+-+-+-+-+-"
	@echo "--> isort" && $(VENVPATH)/isort --profile black -l $(LINT_MAX_LINE_LENGTH) $(SRC_DIR) $(TEST_DIR)
	@echo "-+-+-+-+-+-+-+-+-+-+-+-+-"
	@echo "--> black" && $(VENVPATH)/black -C --line-length $(LINT_MAX_LINE_LENGTH) --target-version py310 $(SRC_DIR) $(TEST_DIR)
	@echo "-+-+-+-+-+-+-+-+-+-+-+-+-"
	@echo "--> autopep8" && $(VENVPATH)/autopep8 -r -i --max-line-length $(LINT_MAX_LINE_LENGTH) $(SRC_DIR) $(TEST_DIR)
	@echo "-+-+-+-+-+-+-+-+-+-+-+-+-"

lint: format
	@echo "--> pylint" && $(VENVPATH)/pylint $(SRC_DIR) $(TEST_DIR) || true
	@echo "-+-+-+-+-+-+-+-+-+-+-+-+-"
	@echo "--> flake8" && $(VENVPATH)/flake8 --max-line-length=$(LINT_MAX_LINE_LENGTH) $(SRC_DIR) || true
	@echo "-+-+-+-+-+-+-+-+-+-+-+-+-"
	@echo "--> mypy" && $(VENVPATH)/mypy --python-version 3.8 --ignore-missing-imports $(SRC_DIR) $(TEST_DIR) || true
	@echo "-+-+-+-+-+-+-+-+-+-+-+-+-"
	@echo "--> yamllint" && $(VENVPATH)/yamllint -f parsable \
		docker-compose.yaml \
		logging.yaml \
		| grep -v "line-length" || true

test:
	@$(VENVPATH)/pytest $(TEST_DIR) --cov $(SRC_DIR) --capture=no
