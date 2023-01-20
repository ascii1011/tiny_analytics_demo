#!/bin/bash
python3 -m venv /opt/app3/venv
. /opt/app3/venv/bin/activate
pip install -r requirements.txt

# python manage.py  ### (also has same ip/port/reload/debug )flask run -h 0.0.0.0 -p 5000
