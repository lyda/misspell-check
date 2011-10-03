#!/bin/bash

# A not very efficient script for searching all man pages
# for misspellings.  It uses the list of words in Wikipedia's
# list of common misspellings to find words that are misspelled.
# http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings/For_machines
# There are a few false positives, but it's easier than using spell(1).

dir="$1"
shift
if [[ -z "$dir" ]]; then
  echo Must give a directory.
  exit 1
fi

while read word; do
  grep -w "$word" misspellings.corrected
  fgrep -lw "$word" "$@" \
    | sed 's/^/  /'
done < misspellings.$dir.dict
