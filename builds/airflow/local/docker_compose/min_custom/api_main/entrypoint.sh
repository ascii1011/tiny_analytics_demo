#!/bin/bash

#echo "OPENAI_API_ORG_ID:"
#echo "${OPENAI_API_ORG_ID}"

#echo "OPENAI_API_KEY:"
#echo "${OPENAI_API_KEY}"

#pip3 install --no-cache-dir --upgrade -r /opt/app/requirements.txt

bash /opt/app/app3/install.sh
bash /opt/app/install.sh

echo 'tailing...'
tail -f /dev/null
