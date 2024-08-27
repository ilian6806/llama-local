#!/bin/bash

while getopts ":a" opt; do
  case $opt in
    a) attach=1 ;;
    ?) echo "Invalid option"; exit 1;;
  esac
done

echo "Closing all llama screens..."

# Close all llama screens
for session in $(screen -ls | grep 'llama3' | awk '{print $1}')
do
  screen -S "${session}" -X quit
done

echo "Starting new screen and gradio server..."

# Relaunch gradio screen and start server
screen -dmS llama3
screen -S llama3 -X stuff 'venv; gradio gradio_start.py\n'

if [ -n "$attach" ]; then
  screen -r llama3
fi

echo "Gradio server started."

### Usable commands ###
# screen -S llama3   - create and attach
# screen -r          - list or join if one
# screen -ls         - list

### Inside screen ###
# ctrl D             - kill
# ctrl AD            - detach
