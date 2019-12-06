# Cognate

Oftentimes we need to develop, test or use applications that target operating systems (versions) other than the one we use in a daily basis. In order to save both time and money deploying and provisioning VMs on public clouds, we should be able to develop or test applications targeting these systems first locally (using some sort of virtualization mechanism) and only then start deploying them elsewhere.

This project aims to use [Virtualbox](https://www.virtualbox.org/), [Vagrant](https://www.vagrantup.com/), [Ansible](https://docs.ansible.com/ansible/latest/index.html) and templated YAML files to deliver a **safe, reproducible and *ideally* idempotent way of providing (*i.e.* creating and managing) and provisioning (*i.e.* installing dependencies and configuring OS internals) local VMs**.

## Dependencies

* [Virtualbox](https://www.virtualbox.org/)
* [Vagrant](https://www.vagrantup.com/)
* [Ansible](https://docs.ansible.com/ansible/latest/index.html)
* [Git](https://git-scm.com/)
* Privileged access (**only if** you wish to mount NFS sharing between host and guest on Virtualbox)

> **Obs:** If you already have Ansible and Git installed, you can refer to the Ansible [alsfreitaz/virtualization](https://github.com/alsfreitaz/virtualization) project to install Virtualbox and Vagrant in an automated and reproducible way.

## Execution

```bash
$ git clone https://github.com/alsfreitaz/cognate.git
$ cd cognate
$ cp vagrant_inventory/hosts.yml.example vagrant_inventory/hosts.yml
$ vagrant up
```

The above commands will provide [two local VMs](https://github.com/alsfreitaz/cognate/blob/master/vagrant_inventory/hosts.yml.example) with given CPU, memory and IP values and provision them with Ansible using a simple example [Ansible playbook](https://github.com/alsfreitaz/cognate/blob/master/provisioning/example/main.yml) and an [Ansible static inventory](https://github.com/alsfreitaz/cognate/blob/master/provisioning/example/inventory.yml) present in the [example](https://github.com/alsfreitaz/cognate/tree/master/provisioning/example) folder.

If all dependencies are met, you should be able to see each instance's name and IP printed to stdout by Ansible [debug module](https://docs.ansible.com/ansible/latest/modules/debug_module.html) at the [Vagrant provision](https://www.vagrantup.com/docs/cli/provision.html) step (automatically invoked by the `vagrant up` command).

## Description

This module relies on the presence of Vagrant and Virtualbox on the machine where the `vagrant` command is to be run.

The code in the [Vagrantfile](https://github.com/alsfreitaz/cognate/blob/master/Vagrantfile) iterates sequentially over all files ended in \*.yml and \*.yaml in vagranat_inventory folder, extracts informations about cpu, memory, private IP, Ansible config file path, Ansible inventory file path and Ansible playbook file path for each VM, provides it with Virtualbox and them provision it with Ansible.

## Supported Systems

Currently, this project was tested on a MacOS X system but should be able to be run on any \*nix system as there are no hard dependencies other than Virtualbox and Vagrant.
