# 0x0F. Load balancer
## Resources :books:
### Read or watch:

* [Introduction to load-balancing and HAproxy]()
* [HTTP header]()
* [Debian/Ubuntu HAProxy packages]()
## Requirements :white_check_mark:
### General
* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 16.04 LTS
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass Shellcheck (version 0.3.7) without any error
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing
* Your servers
* Name	Username	IP	State
* 1623-web-01	ubuntu	35.231.95.4	running	Soft reboot	Hard reboot	Last: Ask a new server
* 1623-web-02	ubuntu	54.175.222.196	running	Soft reboot	Hard reboot	Ask a new server
* 1623-lb-01	ubuntu	54.208.67.225	running	Soft reboot	Hard reboot	Ask a new server
## Tasks
### Mandatory :page_with_curl:
- [x] **[0. Double the number of webservers](./0-custom_http_response-header)** - Since we’re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks
- [x] **[1. Install your load balancer](./1-install_load_balancer)** - Install and configure HAproxy on your lb-01 server
### Advance :muscle:
- [x] **[2. Add a custom HTTP header with Puppet](./2-puppet_custom_http_response-header.pp)** - Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet
## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)
