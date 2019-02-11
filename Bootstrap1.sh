#!/bin/sh
apt-get update -y
apt-get install -y build-essential
apt-get install -y python-dev python-pip
apt-get install -y virtualenv
# apt-get install -y python3-dev python3-pip
curl -sL https://deb.nodesource.com/setup_8.x | bash -
apt-get install -y nodejs
apt-get install -y npm
npm install -g eslint
npm install -g less
npm install -g csslint
# pip install --upgrade pip
# hash pip
