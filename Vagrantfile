script1 = <<'SCRIPT'
apt-get update -y
apt-get install -y build-essential
apt-get install -y python-dev python-pip
apt-get install -y virtualenv
apt-get install -y python3-dev python3-pip
curl -sL https://deb.nodesource.com/setup_8.x | bash -
apt-get install -y nodejs
apt-get install -y npm
npm install -g eslint
npm install -g less
npm install -g csslint
SCRIPT

script2 = <<'SCRIPT'
test -d sdk || git clone https://github.com/edx/xblock-sdk.git sdk
test -d venv || virtualenv venv
. venv/bin/activate
pip install tox
pip install -e ./sdk/
sed -i.bak "s/'[_a-z]\+ *= *sample_xblocks\.\(basic\.\(problem\|content\|slider\)\|.*thumbs\)/\# &/g" sdk/setup.py
sed -i.bak 's/.*acid-block\.git/# &/g' sdk/requirements/dev.txt
pip install -e ./sdk/
pip install -qr ./sdk/requirements/local.txt --exists-action w
pip install -qr ./sdk/requirements/dev.txt --exists-action w
pip install -e ./xblock/
cd sdk && python ./manage.py migrate
SCRIPT

Vagrant.configure('2') do |config|
  # Creates an edX devstack VM from an official release
  config.vm.box     = 'ubuntu/xenial64'
  config.ssh.insert_key = true
  config.vm.synced_folder  ".", "/home/vagrant/xblock", disabled: false
  config.vm.provision 'shell', inline: script1, privileged: true
  config.vm.provision 'shell', inline: script2, privileged: false
  config.vm.network :forwarded_port, guest: 8000, host: 8000
end
