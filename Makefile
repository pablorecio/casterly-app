pc:
	pre-commit run -a

test:
	pytest

deps:
	python -m pip install --upgrade pip; pip install -r receipt_parser/requirements.txt;

sv:
	sam validate --lint

sb:
	sam build

deploy-test: sb
	sam deploy --parameter-overrides 'Env=test' --no-fail-on-empty-changeset --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM --stack-name casterly-app-test

deploy-dev: sv sb
	sam deploy --parameter-overrides 'Env=dev' --no-fail-on-empty-changeset --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM --stack-name casterly-app-dev

deploy-live: sv sb
	sam deploy --parameter-overrides 'Env=live' --no-fail-on-empty-changeset --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM --stack-name casterly-app-live
