#!/bin/bash
. /opt/venv/bin/activate
flask run -h 0.0.0.0 -p 5000 --reload --debugger
