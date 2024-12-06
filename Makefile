install:
	# install dependencies using pip and upgrade pip
	pip install --upgrade pip && pip install -r requirements.txt
format:
	# format code
	black src/
lint:
	# lint code
	pylint --exit-zero --disable=R,C src/
test:
	# run all tests
	python -m tests
coverage:
	# run coverage
	coverage run -m unittest discover -s tests
	coverage report -m
all: format lint test coverage