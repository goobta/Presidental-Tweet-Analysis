#!/bin/bash

docker run -it -p 5000:5000 -v `pwd`/server:/home/jovyan ds3001:project python app.py
