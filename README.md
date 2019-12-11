# Cognate

Oftentimes we need to develop, test or use applications that target operating systems (versions) other than the one we use in a daily basis. In order to save both time and money with VM deploying and provisioning on public clouds, we should be able to develop or test applications targeting these systems first locally (using some sort of virtualization mechanism) and only then start deploying them elsewhere.

This project aims to use [Virtualbox](https://www.virtualbox.org/), [Vagrant](https://www.vagrantup.com/), [Ansible](https://docs.ansible.com/ansible/latest/index.html) and templated YAML files to deliver **a safe, reproducible and *ideally* idempotent way of providing (*i.e.* creating and managing) and provisioning (*i.e.* installing dependencies and configuring OS internals) Virtual Machines locally**.

## Dependencies

* [Virtualbox](https://www.virtualbox.org/)
* [Vagrant](https://www.vagrantup.com/)
* [Ansible](https://docs.ansible.com/ansible/latest/index.html)
* [Git](https://git-scm.com/)
* Privileged access (**only if** you wish to mount NFS sharing between host and guest on Virtualbox)

> **Obs:** If you already have Ansible and Git installed and want to install Virtualbox and Vagrant in an automated and reproducible way, you can check project [alsfreitaz/virtualization](https://github.com/alsfreitaz/virtualization) out.

## Execution

```bash
$ git clone https://github.com/alsfreitaz/cognate.git
$ cd cognate
$ cp vagrant_inventory/hosts.yml.example vagrant_inventory/hosts.yml
$ vagrant up
```

The above commands will provide [two VM](vagrant_inventory/hosts.yml.example) with given CPU, memory and IP values and provision them with Ansible using a simple example [Ansible playbook](provisioning/example/main.yml) and an [Ansible static inventory](provisioning/example/inventory.yml) present in the [example](provisioning/example) folder.

If all dependencies are met, you should be able to see each instance's name and IP printed to stdout by Ansible [debug module](https://docs.ansible.com/ansible/latest/modules/debug_module.html) at the [Vagrant provision step](https://www.vagrantup.com/docs/cli/provision.html) (automatically invoked by the `vagrant up` command).

## Description

This module relies on the presence of Vagrant and Virtualbox on the machine where the `vagrant` command is to be run.

The code in the [Vagrantfile](Vagrantfile) *iterates sequentially* over all files ended in \*.yml and \*.yaml in [vagrant_inventory](vagrant_inventory) folder and, *for each VM declaration*, provides it with Virtualbox using the specified `cpus`, `memory`, `ip`, `box`, `box_version` and `synced_folders` arguments. At the provisioning step (last step executed after VM creation), vagrant will provision the VM with Ansible using the `ansible_config_file`, `ansible_playbook` and `ansible_inventory` file path arguments.

## Supported Systems

Currently, this project was tested on a MacOS X system but should be able to be run on any \*nix system as there are no hard dependencies other than Virtualbox and Vagrant.
