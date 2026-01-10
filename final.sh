#!/usr/bin/bash

for tipo in $(ls out)
do
	echo $tipo
	pdfunite out/$tipo in/reversos/$tipo enviar/$tipo
done
