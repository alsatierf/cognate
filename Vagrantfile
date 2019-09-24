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
      node["synced_folders"].each do |folder|
	if folder["type"] == "rsync" 
          config.vm.synced_folder folder["src"], folder["dest"], type: folder["type"], disabled: folder["disabled"]
	elsif folder["type"] == "nfs"
          config.vm.synced_folder folder["src"], folder["dest"], type: folder["type"], nfs_version: folder["nfs_version"], nfs_udp: folder["nfs_udp"], disabled: folder["disabled"]
        end
      end 
      machine.vm.provider config_file["provider"] do |provider|
        provider.memory = node["memory"]
        provider.cpus = node["cpus"]
      end
      machine.vm.provision :ansible do |ansible|
        ansible.config_file = config_file["ansible_config_file"]
        ansible.inventory_path = node["ansible_inventory"]
        ansible.playbook = node["ansible_playbook"]
      end
    end
  end
end
