#!/bin/bash
NB_ERROR=`grep -e '.*[a-zA-Z0-9]  .*' -x -I $1 -c`

if [[ $NB_ERROR == 0 ]]; then
	exit 0
else
	grep -e '.*[a-zA-Z0-9]  .*' -x -H -n -I $1
	exit $(($NB_ERROR+0))
fi
