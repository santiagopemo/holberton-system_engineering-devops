# 0x0B. SSH
## Resources :books:
### Read or watch:

* [What is a (physical) server - text]()
* [What is a (physical) server - video]()
* [SSH essentials]()
* [SSH Config File]()
* [Public Key Authentication for SSH]()
* [How Secure Shell Works]()
* [SSH Crash Course (Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)]()
* [For reference:]()

* [Understanding the SSH Encryption and Connection Process]()
* [Secure Shell Wiki]()
* [IETF RFC 4251 (Description of the SSH Protocol)]()
* [Internet Engineering Task Force]()
* [Request for Comments]()
### man or help:

* [ssh]()
* [ssh-keygen]()
* [env]()
## Learning Objectives :bulb:
* At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
* What is a server
* Where servers usually live
* What is SSH
* How to create an SSH RSA key pair
* How to connect to a remote host using an SSH RSA key pair
* The advantage of using #!/usr/bin/env bash instead of /bin/bash
## Requirements :white_check_mark:
### General
* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 16.04 LTS
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing
* Your servers
* Name	Username	IP	State
* 1623-web-01	ubuntu	35.237.36.104	running	Soft reboot	Hard reboot	Ask a new server
## Tasks
### Mandatory :page_with_curl:
- [x] **[0. Use a private key](./0-use_a_private_key)** - Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/holberton with the user ubuntu
- [x] **[1. Create an SSH key pair](./1-create_ssh_key_pair)** - Write a Bash script that creates an RSA key pair
- [x] **[2. Client configuration file](./2-ssh_config)** - Your Ubuntu Vagrant machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file
- [x] **[3. Let me in!](./)** - Now that you have successfully connected to your server, we would also like to join the party
### Advance :muscle:
- [x] **[4. Client configuration file (w/ Puppet)](./4-puppet_ssh_config.pp)** - Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password
## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)
