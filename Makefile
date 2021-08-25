install:
	pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
	pip install -r ./requirements.txt

.PHONY: smoke_test
smoke_test:
	(cd Chapter02 && rasa train)
	(cd Chapter03 && rasa train)
	(cd Chapter04 && rasa train)
	(cd Chapter05 && rasa train)
	(cd Chapter06 && rasa train)
	(cd Chapter07 && rasa train)

.PHONY: clean_models
clean_models:
	(cd Chapter02 && rm -rf models)
	(cd Chapter03 && rm -rf models)
	(cd Chapter04 && rm -rf models)
	(cd Chapter05 && rm -rf models)
	(cd Chapter06 && rm -rf models)
	(cd Chapter07 && rm -rf models)


.PHONY: clean
clean:
    ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache