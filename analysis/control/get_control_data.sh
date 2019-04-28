#!/bin/sh

docker run -it -v `pwd`/GOT:/proj -v `pwd`/get_control.py:/proj/get_control.py python:2 bash
