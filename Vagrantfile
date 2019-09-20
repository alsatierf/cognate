# encoding: utf-8
# -*- mode: ruby -*-
# vi: set ft=ruby :

require 'yaml'

VAGRANT_INVENTORY_PATH = "vagrant_hosts.yml"

# Load settings from the Vagrant inventory file
config_file = YAML.load_file("#{File.dirname(File.expand_path(__FILE__))}/#{VAGRANT_INVENTORY_PATH}")

Vagrant.configure(2) do |config|
  config_file["hosts"].each do |node|
    config.vm.define node["name"] do |machine|
      machine.vm.box = node["box"]
      machine.vm.box_check_update = false
      machine.vm.network "private_network", ip: node["ip"]
      machine.vm.provider config_file["provider"] do |provider|
        provider.memory = node["memory"]
        provider.cpus = node["cpus"]
      end
      machine.vm.provision :ansible do |ansible|
	ansible.compatibility_mode = "2.0"
        ansible.inventory_path = node["ansible_inventory"]
        ansible.playbook = node["ansible_playbook"]
      end
    end
  end
end
