#!/bin/sh

cp get_control.py GOT/

docker run -it -v `pwd`/GOT:/proj -v `pwd`/get_control.py:/proj/get_control.py ds3001:got

mv -f GOT/control_tweets.csv .
rm GOT/get_control.py 
