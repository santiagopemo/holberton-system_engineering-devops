# 0x14. MySQL
## Resources :books:
### Read or watch:

* [What is a primary-replica cluster]()
* [MySQL primary replica setup]()
* [Build a robust database backup strategy]()
### man or help:

* [mysqldump]()
## Learning Objectives :bulb:
* At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
* What is the main role of a database
* What is a database replica
* What is the purpose of a database replica
* Why database backups need to be stored in different physical locations
* What operation should you regularly perform to make sure that your database backup strategy actually works
## Requirements :white_check_mark:
### General
* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 16.04 LTS
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing
* Your servers
* Name	Username	IP	State
* 1623-web-01	ubuntu	35.231.95.4	running	Soft reboot	Hard reboot	Last: Ask a new server
* 1623-web-02	ubuntu	54.175.222.196	running	Soft reboot	Hard reboot	Ask a new server
* 1623-lb-01	ubuntu	54.208.67.225	running	Soft reboot	Hard reboot	Ask a new server
## Tasks
### Mandatory :page_with_curl:
- [x] **[0. Install MySQL](./) - First things first, let’s get MySQL installed on both your web-01 and web-02 servers.
- [x] **[1. Let us in!](./) - In order for us to verify that your servers are properly configured, we need you to create a user and password for both MySQL databases which will allow the checker access to them.
- [x] **[2. If only you could see what I've seen with your eyes](./) - In order for you to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.
- [x] **[3. Quite an experience to live in fear, isn't it?](./) - Before you get started with your primary-replica synchronization, you need one more thing in place. On your primary MySQL server (web-01), create a new user for the replica server.
- [x] **[4. Setup a Primary-Replica infrastructure using MySQL](./4-mysql_configuration_primary)** - First things first, let’s get MySQL installed on both your web-01 and web-02 servers
- [x] **[5. MySQL backup](./5-mysql_backup)** - What if the data center where both your primary and replica database servers are hosted are down because of a power outage or even worse: flooding, fire? Then all your data would inaccessible or lost. That’s why you want to backup and store them in a different system in another physical location. This can be achieved by dumping your MySQL data, compressing them and storing them in a different data center
## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)
