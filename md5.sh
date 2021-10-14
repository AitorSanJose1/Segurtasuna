#!/bin/bash
	var=$(cat probamd5.txt)
	fitx=$(md5sum proba.txt)
	
	if [[ $var =~ $fitx ]]; then
		echo "Aurkituta"
		echo "$var"
	else
		echo "$var"
		echo "Artxiboa aldatu da"
		
	fi
