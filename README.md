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

## Quick Virtual Machine Providing and Provisioning Example

In order to make a quick check on how to use this framework, plese run the following:

```bash
$ git clone https://github.com/alsfreitaz/cognate.git
$ cd cognate
$ cp vagrant_inventory/hosts.yml.example vagrant_inventory/hosts.yml
$ vagrant up
```

The above commands will provide [two virtual machines](vagrant_inventory/hosts.yml.example) with given CPU, memory and IP values and then provision them with Ansible from an example [Ansible playbook](provisioning/example/main.yml) and an [Ansible static inventory](provisioning/example/inventory.yml) present in the [example](provisioning/example) folder.

If all dependencies are met, you should be able to see each instance's name and IP printed to stdout by Ansible's [debug module](https://docs.ansible.com/ansible/latest/modules/debug_module.html) at the [Vagrant provision step](https://www.vagrantup.com/docs/cli/provision.html) (automatically invoked by the `vagrant up` command).

## Framework Internals

This module relies on the presence of Vagrant and Virtualbox on the machine where the `vagrant` command is to be run, so if you didn't install both of them yet, please refer to the [Dependencies](#dependencies) section.

The code in the [Vagrantfile](Vagrantfile) *iterates sequentially* over all files ended in \*.yml and \*.yaml in [vagrant_inventory](vagrant_inventory) folder and, *for each VM declaration*, provides it with Virtualbox using the specified `name`, `ip`, `cpus`, `memory`, `box`, `box_version` and `synced_folders` arguments. At the provisioning step (last step executed after VM creation), vagrant will provision the VM with Ansible using the `ansible_config_file`, `ansible_playbook` and `ansible_inventory` file path arguments.

> One key point to notice is that **both** `name` **and** `ip` **arguments** in a vagrant_inventory/\*.yml file **must match the corresponding host and ip** Ansible arguments the corresponding `ansible_playbook` parameter points to. In order to figure out how this works in practice, please check how the two `ip` and `name` parametes on file vagrant_inventory/hosts.yml.example relate to `hosts` and `ansible_ssh_host` parameters on example/inventory.yml on the [Providing and Provisioning Example](#providing-and-provisioning-example).

## Further Usage

### Development, Prototyping and Testing

One effective way of using this framework for developing, prototyping and testing is to follow these steps:

1. Clone this repository (if you didn't do that up to this moment) and enter the project root folder:

    ```bash
    $ git clone https://github.com/alsfreitaz/cognate.git
    $ cd cognate
    ```
    
2. Create a folder under the [provisioning](provisioning) folder
3. Create or drop existing Ansible files (specially ansible.cfg, playbooks and inventories) under the new folder and assign some hostnames and IP addresses in a private range.
4. Create a \*.yaml or \*.yml file under [vagrant_inventory](vagrant_inventory) using the [template file](vagrant_inventory/hosts.yml.template) or the [example file](vagrant_inventory/hosts.yml.example) as reference and point the correct `name` and `ip` paramentes to the corresponding hostnames and IPs in the inventory from step 2
5. Run `vagrant up` on this project root folder to provide and provision all machines.

> Obs: After providing a MV, if something goes wrong at the provisioning step (automatically executed by the command `vagrant up` when the machine is created the first time) or if you just want to run the provisioning step without having to destroy and recreate the machine(s), just run the command `vagrant provision <vm_name>` to provision a specific machine or `vagrant provision` to provision all machines with status `created` in vagrant.

## Supported Systems

Currently, this project was tested on a MacOS X system but should be able to be run on any system where vagrant is installed as it simply acts as a predefined Vagrantfile configuration step to be used by pure vagrant. 
