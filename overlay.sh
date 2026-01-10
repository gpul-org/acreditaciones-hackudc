#!/usr/bin/bash

for tipo in $(ls QR)
do
	echo $tipo
	for qr in $(ls QR/$tipo/)
	do
		python3 overlay.py $tipo $qr
	done
done
