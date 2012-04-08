#!/bin/bash

echo 'Remember to manually edit this list.'

url="http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings/For_machines"
wget -O - "$url" 2>| /dev/null \
  | sed -n '/<pre>/,/<\/pre>/p' \
  | sed 's/   */ /g' \
  | sed "s/'/\\\'/g;s/\(.*\)-.gt;\(.*\)/    '\1': ['\2'],/;s/, /', '/g" \
  | sed '1d;$d' \
  | grep -v "^'ok' "
