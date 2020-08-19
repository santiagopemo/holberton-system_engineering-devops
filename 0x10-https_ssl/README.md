# 0x10. HTTPS SSL
## Resources :books:
### Read or watch:

* [What is HTTPS?]()
* [What are the 2 main elements that SSL is providing]()
* [HAProxy SSL termination on Ubuntu16.04]()
* [SSL termination]()
* [Bash function]()
### man or help:

* [awk]()
* [dig]()
## Learning Objectives :bulb:
* At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
* What is HTTPS SSL 2 main roles
* What is the purpose encrypting traffic
* What SSL termination means
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
- [x] **[0. HTTPS ABC](./0-https_abc)** - As for project 0x07, use numbers in your answer file
- [x] **[1. World wide web](./1-world_wide_web)** - Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains
- [x] **[2. HAproxy SSL termination](./2-haproxy_ssl_termination)** - “Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination
### Advance :muscle:
- [x] **[3. No loophole in your website traffic](./100-redirect_http_to_https)** - A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS
## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)
