# -*- mode: ruby -*-
# vi: set ft=ruby :

BASE_BOX = "nefarioustim/nefarious-base"
IP_ADDRESS = "33.33.33.30"
GUEST_LOCATION = "/home/vagrant/parker"
MEMORY = "512"
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = BASE_BOX
    config.vm.network :private_network, ip: IP_ADDRESS
    config.vm.synced_folder ".", GUEST_LOCATION, :nfs => true
    config.ssh.forward_agent = true

    config.vm.provider "virtualbox" do |my_vm|
        my_vm.customize ["modifyvm", :id, "--memory", MEMORY]
    end

    config.vm.provision :shell do |shell|
        shell.inline = "cd #{GUEST_LOCATION}/puppet && librarian-puppet update"
    end

    config.vm.provision :puppet do |puppet|
        puppet.options = "-v"
        puppet.manifests_path = "puppet/manifests"
        puppet.manifest_file  = "dev.pp"
        puppet.module_path = "puppet/modules"
    end

    config.vm.provision :shell do |shell|
        shell.inline = "cd #{GUEST_LOCATION} && make install"
    end
end
