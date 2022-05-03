build:
	python3 setup.py sdist bdist_wheel --universal
clean:
	rm -rf build dist *.egg-info */__pycache__
upload:
	twine upload dist/*
install:
	python3 setup.py install
release: clean build upload
