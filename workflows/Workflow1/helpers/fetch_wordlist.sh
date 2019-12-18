#!/usr/bin/env bash


GIST="https://gist.githubusercontent.com/bwbaugh/bf78612ef58ad0402a05/raw/0f8ea7a054ff5c9c4209414beadf7a3acdd03373/server-name-wordlist-mnemonic.txt"
CDATA=../cdata
curl $GIST | tail --lines +4 | shuf > $CDATA/server-name-wordlist-mnemonic.txt 
