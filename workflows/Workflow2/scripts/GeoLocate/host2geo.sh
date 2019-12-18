#!/bin/bash

JAVA="/usr/bin/java"

if [[ $# -ne 3 ]] 
then
	echo "Usage: <name|ip> <output_file> <err_log_file>"
	exit 1
fi

LIST=$1
GEO=$2
LOG=$3

cat $LIST | while read HOST
do
	$JAVA -cp "./scripts/GeoLocate/GeoMaxMind:./scripts/GeoLocate"  ISSCityLookup ./cdata/GeoLocate/GeoLiteCity.dat $HOST 1>> $GEO 2>>$LOG
	if [[ $? != 0 ]]
	then
		echo "$HOST: geo failed" >>  $LOG
	fi
done

