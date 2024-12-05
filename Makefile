install:
	# install dependencies using pip and upgrade pip
	pip install --upgrade pip && pip install -r requirements.txt
format:
	# format code
	black **/*.py
lint:
	# lint code
	pylint --disable=R,C **/*.py
test:
	# run all tests
	python -m tests
coverage:
	# run coverage
	coverage run -m unittest discover -s tests
	coverage report -m