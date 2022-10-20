test:
	echo "remember to run the environment set up script"
	python3 -m pytest `pwd`/src/tests/*

lint:
	autopep8 --in-place --aggressive src/objects/*.py
	autopep8 --in-place --aggressive src/tests/*.py
	autopep8 --in-place --aggressive src/functions/*.py

clean:
	rm *.ppm

#image is upside down and needs to be flipped vertically
