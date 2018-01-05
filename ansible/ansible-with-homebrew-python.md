# Ansible with Homebrew Python

Usually when using Ansible, it will execute the modules specified in the playbooks on the remote host using Python. The Python binary is not selected using the usual `/usr/bin/env python` but instead is set in the `ansible_python_interpreter` inventory variable. This variable defaults to `/usr/bin/python`. 

Most of the time when managing Linux hosts, this works perfectly fine, but when using many network automation modules the modules are executed locally on the host where Ansible is running (`ansible_connection = local`). On macOS, this is particularly confusing if Python is installed by Homebrew as you will have two Python binaries - one in `/usr/bin/python` and one in `/usr/local/bin/python` with the latter being preferred by the shell and the first being selected by Ansible. This leads to the confusing situation where Ansible runs will fail with errors about missing Python dependencies but `pip list` shows them already installed. 

The easiest solution is to setup ~/.ansible.cfg like the following:
```ini
[defaults]

ansible_python_interpreter = /usr/local/bin/python
```
