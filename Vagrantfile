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
sudo -u vagrant pip install tox
sudo -u vagrant git clone https://github.com/edx/xblock-sdk.git /home/vagrant/sdk
SCRIPT

Vagrant.configure('2') do |config|
  # Creates an edX devstack VM from an official release
  config.vm.box     = 'ubuntu/xenial64'
  config.ssh.insert_key = true
  config.vm.synced_folder  ".", "/home/vagrant/xblock", disabled: false
  config.vm.provision "shell", inline: $script
end
