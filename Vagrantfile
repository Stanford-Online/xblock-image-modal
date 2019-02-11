Vagrant.configure('2') do |config|
  # Creates an edX devstack VM from an official release
  config.vm.box     = 'ubuntu/xenial64'
  config.ssh.insert_key = true
  config.vm.synced_folder  ".", "/home/vagrant/xblock", disabled: false
  config.vm.provision "shell", path: 'Bootstrap1.sh', privileged: true
  config.vm.provision "shell", path: 'Bootstrap2.sh', privileged: false
  config.vm.network :forwarded_port, guest: 8000, host: 8000
end
