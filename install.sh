#!/bin/bash
sudo apt install git
sudo apt install python3
sudo apt install pip
pip install python-aternos
cd ~/
mkdir AternosClient
cd AternosClient
git clone https://github.com/Paperozza/AthernosScript.git

LATEST_RELEASE=$(curl -L -s -H 'Accept: application/json' https://github.com/North-West-Wind/CurseForge-CLI/releases/latest)

LATEST_VERSION=$(echo $LATEST_RELEASE | sed -E 's/.*"tag_name":"\([^"]*\)".*/\1/')
ARTIFACT_URL="https://github.com/North-West-Wind/CurseForge-CLI/releases/tag/$LATEST_VERSION/curseforge.zip"