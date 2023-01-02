#!/bin/bash
python -m venv /opt/venv
. /opt/venv/bin/activate
pip install -r requirements.txt

#flask run -h 0.0.0.0 -p 5000
