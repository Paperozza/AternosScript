#!/bin/bash
sudo apt install git
sudo apt install python3
sudo apt install pip
pip install python-aternos
cd ~/
mkdir AternosClient
cd AternosClient
git clone https://github.com/Paperozza/AthernosScript.git


alias atclient="python3 ~/AternosClient/AthernosScript/Script.py"
