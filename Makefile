pc:
	pre-commit run -a

test:
	pytest

deps:
	python -m pip install --upgrade pip; pip install -r invoice_parser/requirements.txt;
