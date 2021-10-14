#!/bin/bash
for var in ./irudia/* ;
 do
 	
	hash="e5ed313192776744b9b93b1320b5e268" 
	irudi=$(md5sum $var)

	if [[ $irudi =~ $hash ]]; then
		echo "Artxiboa aurkitu da"
		echo  "$var"		
	
	fi	

done
