# 0x0A Configuration management
## Resources :books:
### Read or watch:

* [Intro to Configuration Management]()
* [Puppet resource type: file (check “Resource types” for all manifest types in the left menu)]()
* [Puppet’s Declarative Language: Modeling Instead of Scripting]()
* [Puppet lint]()
* [Puppet emacs mode]()
## Requirements :white_check_mark:
### General
* All your files will be interpreted on Ubuntu 14.04 LTS
* All your files should end with a new line
* A README.md file at the root of the folder of the project is mandatory
* Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
* Your Puppet manifests must run without error
* Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
* Your Puppet manifests files must end with the extension .pp
* Note on Versioning
* Your Ubuntu 14.04 VM should have Puppet 3.4 preinstalled.

* You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

* The linked documentation is to Puppet 3.8 because the 3.4 documentation has been archived and is therefore more challenging to navigate. If you would like to upgrade anyway, click here (this will not affect how your code is checked). Puppet 5 Docs

* Install puppet-lint
* $ apt-get install -y ruby
* $ gem install puppet-lint -v 2.1.1
## Tasks
### Mandatory :page_with_curl:
- [x] **[0. Create a file](./0-create_a_file.pp)** - Using Puppet, create a file in /tmp
- [x] **[1. Install a package](./1-install_a_package.pp)** - Using Puppet, install puppet-lint
- [x] **[2. Execute a command](./2-execute_a_command.pp)** - Using Puppet, create a manifest that kills a process named killmenow
## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)
