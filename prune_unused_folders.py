#!/usr/bin/env python

import subprocess
import os
import shutil

machine_folders = subprocess.run(["ls", ".vagrant/machines"], stdout=subprocess.PIPE, universal_newlines=True)
existing_machines = subprocess.run("vagrant global-status --prune | grep $(realpath .) | sed -E 's/[ ]+/ /g' | cut -d' ' -f2 | sort", shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)

unused_folders = set(str(machine_folders.stdout).split('\n')) - set(str(existing_machines.stdout).split('\n'))

if len(unused_folders) > 0:
    print("Prunning folders {}".format(",".join(unused_folders)))
else:
    print("There are no vagrant machine folders to be prunned. Nothing to do.")
    
for folder in unused_folders:
    shutil.rmtree(os.path.join(".vagrant/machines", folder))