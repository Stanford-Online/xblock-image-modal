$script = <<SCRIPT
apt-get update -y
apt-get install -y build-essential
apt-get install -y python-dev python-pip
apt-get install -y python3-dev python3-pip
curl -sL https://deb.nodesource.com/setup_8.x | bash -
apt-get install -y nodejs
apt-get install -y npm
npm install -g eslint
npm install -g less
npm install -g csslint
sudo -H -u vagrant git clone https://github.com/edx/xblock-sdk.git /home/vagrant/sdk
sudo -H -u vagrant pip install --user pip
sudo -H -u vagrant pip install --user tox
sudo -H -u vagrant pip install --user -e /home/vagrant/xblock/
cd /home/vagrant/sdk
sudo -H -u vagrant pip install --user -e .
sudo -H -u vagrant pip install --user -qr ./requirements/local.txt --exists-action w
sudo -H -u vagrant pip install --user -qr ./requirements/dev.txt --exists-action w
sudo -H -u vagrant python ./manage.py migrate
SCRIPT
# sudo -H -u vagrant python ./manage.py runserver 0.0.0.0:8000

Vagrant.configure('2') do |config|
  # Creates an edX devstack VM from an official release
  config.vm.box     = 'ubuntu/xenial64'
  config.ssh.insert_key = true
  config.vm.synced_folder  ".", "/home/vagrant/xblock", disabled: false
  config.vm.provision "shell", inline: $script
  config.vm.network :forwarded_port, guest: 8000, host: 8000
end
