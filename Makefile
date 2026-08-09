VENV    = .venv
PYTHON  = $(VENV)/bin/python
ifeq ("$(wildcard $(VENV)/bin/python)","")
  PYTHON = python3
endif
RUNNER  = run_tests.py

.PHONY: help install test test-one

help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'

install: ## Create venv and install dependencies (rich) for beautiful logs
	python3 -m venv $(VENV)
	$(VENV)/bin/python -m pip install -r requirements.txt

test: ## Run tests for every solution that has a test_cases.csv
	$(PYTHON) $(RUNNER)

test-one: ## Run tests for one solution: make test-one PROBLEM=TopicWise/Stack/valid_parentheses/main.py
	@test -n "$(PROBLEM)" || (echo "Usage: make test-one PROBLEM=<path/to/main.py>" && exit 1)
	$(PYTHON) $(RUNNER) $(PROBLEM)
