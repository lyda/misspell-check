#!/bin/bash

echo 'Remember to manually edit this list.'

url="http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings/For_machines"
wget -O - "$url" 2>| /dev/null \
  | sed -n '/<pre>/,/<\/pre>/p' \
  | sed 's/-.gt;/, /;1d;$d' \
  | perl -pe 'chomp; @l = split(/, /); $_ = "";
              for ($i = 1; $i <= $#l; $i++) {
                $_ .= "$l[0] $l[$i]\n";
              }' \
  | grep -v '^ok '
