#!/bin/bash

if [[ -z "$1" ]]; then
  echo Must give a directory.
  exit 1
fi

find $1 -type f -print0 | xargs -0 cat \
  | tr ' \t' '\n\n' \
  | grep "^[a-zA-Z']*$" \
  |sort -u >| all-words.$1
join misspellings.dict all-words.$1 > misspellings.$1.dict
