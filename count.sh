#!/bin/bash

#check if the file is present in the current directory
if ! [[ -f 'README' ]]; then 
  #if it's not yet present -> download the file with "wget"
  wget ftp://sunsite.informatik.rwth-aachen.de/pub/mirror/ibiblio/gnome/README  
fi
#read file
cat README |
#make all text lowercase
tr '[:upper:]' '[:lower:]' |#!/bin/bash

#check if the file is present in the current directory
if ! [[ -f 'README' ]]; then 
  #if it's not yet present -> download the file with "wget"
  wget ftp://sunsite.informatik.rwth-aachen.de/pub/mirror/ibiblio/gnome/README  
fi
#read file
cat README |
#make all text lowercase
tr '[:upper:]' '[:lower:]' |
#replace whitespace with new line
sed "s/ /\n/g" |
#remove all empty lines
sed '/^$/d' |
#remove punctation
tr -d [:punct:] |
#alphabetically sort the list of words and remove duplicates
sort | uniq -c |
#print out the 10 most common words in the text on stdout
sort -r | awk '{print $2}' | head -n 10
#replace whitespace with new line
sed "s/ /\n/g" |
#remove all empty lines
sed '/^$/d' |
#remove punctation
tr -d [:punct:] |
#alphabetically sort the list of words and remove duplicates
sort | uniq -c |
#print out the 10 most common words in the text on stdout
sort -r | awk '{print $2}' | head -n 10
