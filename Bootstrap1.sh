#!/bin/sh
whoami
apt-get update -y
apt-get install -y build-essential
apt-get install -y python-dev python-pip
# apt-get install -y python3-dev python3-pip
curl -sL https://deb.nodesource.com/setup_8.x | bash -
apt-get install -y nodejs
apt-get install -y npm
npm install -g eslint
npm install -g less
npm install -g csslint
sudo -H -u vagrant git clone https://github.com/edx/xblock-sdk.git /home/vagrant/sdk
cd /home/vagrant/sdk
sed -i.bak "s/'[_a-z]\+ *= *sample_xblocks\.\(basic\.\(problem\|content\|slider\)\|.*thumbs\)/\# &/g" setup.py
sed -i.bak 's/.*acid-block\.git/# &/g' requirements/dev.txt
pip install --upgrade pip
hash pip
pip install tox
pip install -e /home/vagrant/xblock/
pip install -e .
pip install -qr ./requirements/local.txt --exists-action w
pip install -qr ./requirements/dev.txt --exists-action w
