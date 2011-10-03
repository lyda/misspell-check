This is a series of scripts to check for misspelled
words and is based on the [Wikipedia list of common
misspellings](http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings/For_machines)

The list has been slightly modified to remove some changes that cause
a number of false positives.  In particular `ok->OK` was removed (ok is
frequently used in perl tests for instance).

The way the current scripts work is that you copy them and the data
files into a directory.  Within that directory you checkout a number
of projects into sub-directories.  Then you run `./reduce-dict.sh
a-sub-dir` which generates a list of misspelled words.  Then you run
`./find_misspellings.sh a-sub-dir a-sub-dir/**/*(.)` (in zsh - in less
capable shells you'd use a `$(find ...)` thing).  Note that a-sub-dir
must not have a / in it.  This is not the brightest series of scripts...
