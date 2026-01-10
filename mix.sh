#!/usr/bin/bash

for tipo in $(ls SVG)
do
	echo $tipo
	pdfunite PDF/$tipo/*.pdf out/$tipo.pdf
done
