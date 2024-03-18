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

sv:
	sam validate --lint

sb:
	sam build

deploy-dev: sv sb
	sam deploy --parameter-overrides 'Env=dev' --no-fail-on-empty-changeset --stack-name casterly-app-dev

deploy-live: sv sb
	sam deploy --parameter-overrides 'Env=live' --no-fail-on-empty-changeset --stack-name casterly-app-live
