#!/bin/sh
sudo -H -u vagrant git clone https://github.com/edx/xblock-sdk.git /home/vagrant/sdk
cd /home/vagrant/sdk
sed -i.bak "s/'[_a-z]\+ *= *sample_xblocks\.\(basic\.\(problem\|content\|slider\)\|.*thumbs\)/\# &/g" setup.py
sed -i.bak 's/.*acid-block\.git/# &/g' requirements/dev.txt
virtualenv /home/vagrant/venv
. /home/vagrant/venv/bin/activate
pip install tox
pip install -e /home/vagrant/xblock/
pip install -e .
pip install -qr ./requirements/local.txt --exists-action w
pip install -qr ./requirements/dev.txt --exists-action w
python ./manage.py migrate
