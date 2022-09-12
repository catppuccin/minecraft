#!/bin/bash

for image in *.png
do
	cp $image file.png
	python color.py
	cp output.png $image
	rm file.png output.png
done
