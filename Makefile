test:
	echo "remember to run the environment set up script"
	python3 -m pytest `pwd`/src/tests/*

clean:
	rm *.ppm