#!/usr/bin/bash

for tipo in $(ls SVG)
do
	echo $tipo
	for qr in $(ls SVG/$tipo/)
	do
		inkscape --export-filename=PDF/$tipo/$qr.pdf SVG/$tipo/$qr
		python3 overlay.py $tipo $qr
	done
done
