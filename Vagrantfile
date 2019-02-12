Vagrant.configure('2') do |config|
  # Creates an edX devstack VM from an official release
  config.vm.box     = 'ubuntu/xenial64'
  config.ssh.insert_key = true
  config.vm.synced_folder  ".", "/home/vagrant/xblock", disabled: false
  config.vm.provision "shell" do |s|
    s.privileged = true
    s.path = 'Makefile'
    s.args = [
        'bootstrap',
    ]
  end
  config.vm.provision "shell" do |s|
    s.privileged = false
    s.path = 'Makefile'
    s.args = [
        'go',
    ]
  end
  config.vm.network :forwarded_port, guest: 8000, host: 8000
end
