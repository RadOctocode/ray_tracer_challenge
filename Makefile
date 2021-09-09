test:
	echo "remember to export PYTHONPATH = `pwd`/src/objects"
	python3 -m pytest `pwd`/src/tests/*