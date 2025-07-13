clean:
	@echo 'Removing python self generated unwanted files'
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '*pyo' -exec rm -f {} +
	find . -name '*pyc' -exec rm -f {} +
	find . -name 'ipynb_checkpoints' -exec rn -rf {} +
	find . -name '.DS_Store' -exec rm -rf {} +
	find . -name '.pytest_cache' -exec rm -fr {} +
	find . -name '.coverage' -exec rm -f {} +

start:
	@echo 'Server is starting...'
	dagster dev -w workspace.yaml