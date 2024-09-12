Vagrant.configure(2) do |config|

  # config.ssh.username = "user"
  # config.ssh.password = "changeme" # nothing to find here :)
  config.ssh.insert_key = true

  config.vm.box = "debian/bookworm64"

  config.vm.provider "virtualbox" "virtualbox" do |vb|
    vb.name="rliebig-dev-machine"

    vb.gui=true
    vb.memory = "8096" # uneven number 
    vb.cpus = 8

  end

  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "main.yml"
  end

end
