#!/bin/sh
sudo apt update
sudo apt install python3-dev libpq-dev python3-pip -y
python3 -m pip install -r requirements.txt
python3 -m pip install -e .