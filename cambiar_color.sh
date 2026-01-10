#!/usr/bin/bash

function colorear() {
	for i in $(ls $1)
	do
		sed -i "s/#000000/$2/" $1/$i
	done;
}

colorear QR/hacker "#004e31"
colorear QR/mentor "#16496a"
colorear QR/organizacion "#4e3262"
colorear QR/patrocinador "#772a36"
