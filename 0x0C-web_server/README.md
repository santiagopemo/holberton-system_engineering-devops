# 0x0C. Web server
## Resources :books:
### Read or watch:

* [How the web works]()
* [Nginx]()
* [How to Configure Nginx]()
* [Child process]()
* [Root and sub domain]()
* [HTTP requests]()
* [HTTP redirection]()
* [Not found HTTP response code]()
* [Logs files on Linux]()
### For reference:

* [RFC 7231 (HTTP/1.1)]()
* [RFC 7540 (HTTP/2)]()
### man or help:

* [scp]()
* [curl]()
## Learning Objectives :bulb:
* At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
* What is the main role of a web server
* What is a child process
* Why web servers usually have a parent process and child processes
* What are the main HTTP requests
* DNS
* What DNS stands for
* What is DNS main role
* DNS Record Types
* A
* CNAME
* TXT
* MX
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
## Tasks
### Mandatory :page_with_curl:
- [x] **[0. Transfer a file to your server](./0-transfer_file)** - Write a Bash script that transfers a file from our client to a server
- [x] **[1. Install nginx web server](./1-install_nginx_web_server)** - Web servers are the piece of software generating and serving HTML pages, let’s install one!
- [x] **[2. Setup a domain name](./2-setup_a_domain_name)** - .TECH Domains is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. Holberton School partnered with .TECH Domains so that you can learn about DNS
- [x] **[3. Redirection](./3-redirection)** - Readme
- [x] **[4. Not found page 404](./4-not_found_page_404)** - Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page
### Advance :muscle:
- [x] **[5. Design a beautiful 404 page](./5-design_a_beautiful_404_page)** - Some of my favorites
- [x] **[6. Install Nginx web server (w/ Puppet)](./7-puppet_install_nginx_web_server.pp
)** - Time to practice configuring your server with Puppet! Just as you did before, we’d like you to install and configure an Nginx server using Puppet instead of Bash. To save time and effort, you should also include resources in your manifest to perform a 301 redirect when querying /redirect_me
## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)
