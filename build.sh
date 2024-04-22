#!/bin/bash

# Function to stop processes 
stop_processes() {
    echo "Stopping processes..."
    pkill -SIGINT -f "python3 log.py"
    pkill -SIGINT -f "python3 generate.py"
}

trap 'stop_processes; exit' INT

python3 log.py &
python3 generate.py &

wait
