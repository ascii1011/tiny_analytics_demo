#!/bin/bash

chmod +x *.sh
chmod +x *.py

. ./utils.sh --source-only

onboard


echo 'tailing...'
tail -f /dev/null
