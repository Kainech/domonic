test:
	python3.7 -m unittest tests.test_html
	python3.7 -m unittest tests.test_dom
	python3.7 -m unittest tests.test_style
	python3.7 -m unittest tests.test_javascript
	python3.7 -m unittest tests.test_terminal

build:
	rm -r dist/
	python3 setup.py sdist

deploy:
	rm -r dist/
	python3 setup.py sdist
	twine upload dist/*