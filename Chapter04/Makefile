.PHONY: run_model
run_model:
	rasa run --cors "*" --credentials ./credentials.yml --debug

.PHONY: run_actions
run_actions:
	rasa run actions --debug

.PHONY: install
install:
	bash ./install_dependency.bash

.PHONY: download
download:
	bash ./download_mitie_data.bash
