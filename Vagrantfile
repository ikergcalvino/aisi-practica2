# -*- mode: ruby -*-
# vi: set ft=ruby :
require_relative 'provisioning/vbox.rb'
VBoxUtils.check_version('7.0.6')
Vagrant.require_version ">= 2.3.4"

class VagrantPlugins::ProviderVirtualBox::Action::Network
  def dhcp_server_matches_config?(dhcp_server, config)
    true
  end
end

BOX_NAME = "xxx-aisi2223/focal64"
MANAGER_HOSTNAME = "xxx-aisi2223-docker"
WORKER_HOSTNAME = "xxx-aisi2223-docker-worker"

Vagrant.configure("2") do |config|
  config.vm.box = BOX_NAME

  # Configure hostmanager and vbguest plugins
  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  config.hostmanager.manage_guest = true
  config.vbguest.auto_update = false

  # Manager node
  config.vm.define "manager", primary: true do |manager|
    manager.vm.hostname = MANAGER_HOSTNAME
    manager.vm.network "private_network", ip: "10.10.1.10", virtualbox__intnet: true
    manager.vm.network "forwarded_port", guest: 80, host: 8080
    # manager.vm.provision "shell", path: "provisioning/install-docker-compose-ubuntu.sh"

    manager.vm.provider "virtualbox" do |prov|
        prov.name = "AISI-P2-#{manager.vm.hostname}"
        prov.cpus = 1
        prov.memory = 1024
	prov.gui = false
    end
  end
  
  # Worker node
  config.vm.define "worker" do |worker|
    worker.vm.hostname = WORKER_HOSTNAME
    worker.vm.network "private_network", ip: "10.10.1.11", virtualbox__intnet: true
    worker.vm.network "forwarded_port", guest: 80, host: 9090
            
    worker.vm.provider "virtualbox" do |prov|
	prov.name = "AISI-P2-#{worker.vm.hostname}"
        prov.cpus = 1
        prov.memory = 1024
	prov.gui = false
    end
  end

  config.vm.provision "shell", run: "always", inline: <<-SHELL
	grep -qxF 'export DOCKER_BUILDKIT=0' /home/vagrant/.bashrc || echo 'export DOCKER_BUILDKIT=0' >> /home/vagrant/.bashrc
  SHELL
end
