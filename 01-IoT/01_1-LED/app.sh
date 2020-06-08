#!/bin/bash

export FLASK_APP=/home/pi/app.py
export FLASK_ENV=development
#flask run --host=0.0.0.0

#flask run
nohup flask run --host=0.0.0.0 --port=8000 >> /var/log/flask.log &
