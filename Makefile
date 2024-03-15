pc:
	pre-commit run -a

test:
	pytest

deps:
	python -m pip install --upgrade pip; pip install -r receipt_parser/requirements.txt;

build_lambda:
	cd receipt_parser && mkdir package && pip install --target ./package -r requirements.txt
	cd receipt_parser/package && zip -r ../build.zip .
	cd receipt_parser && rm -r package && zip -r build.zip src
	cd receipt_parser/src && zip ../build.zip main.py
