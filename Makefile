pc:
	pre-commit run -a

test:
	pytest

deps:
	python -m pip install --upgrade pip; pip install -r receipt_parser/requirements.txt;
