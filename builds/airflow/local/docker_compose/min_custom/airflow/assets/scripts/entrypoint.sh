#!/bin/bash

. ./utils.sh --source-only

onboard


echo 'tailing...'
tail -f /dev/null
