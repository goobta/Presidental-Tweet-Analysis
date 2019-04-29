#!/bin/bash

docker run -it -p 5000:5000 \
	         -v `pwd`:/home/jovyan \
					 -w /home/jovyan/server \
					 ds3001:project python app.py
