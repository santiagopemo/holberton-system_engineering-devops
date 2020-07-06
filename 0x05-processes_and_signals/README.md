# 0x05. Processes and signals
## Resources :books:

* [Linux PID](https://intranet.hbtn.io/rltoken/FcpEdqz8hau7eEB0Pi8Ong)
* [Linux process](https://intranet.hbtn.io/rltoken/hX_t2YK0erLPbdTq0-uKwQ)
* [Linux signal](https://intranet.hbtn.io/rltoken/SojW4zvL8j1yaoa7_NM6rA)

## Learning Objectives :bulb:
* What is a PID
* What is a process
* How to find a process’ PID
* How to kill a process
* What is a signal
* What are the 2 signals that cannot be ignored

## Requirements :white_check_mark:
* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 14.04 LTS
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing 

## Tasks :page_with_curl:
### Mandatory
- [x] **[0. What is my PID ](./0-what-is-my-pid )** - Write a Bash script that displays its own PID
- [x] **[1. List your processes](./1-list_your_processes)** - Write a Bash script that displays a list of currently running processes
- [x] **[2. Show your Bash PID](./2-show_your_bash_pid)** - Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process
- [x] **[3. Show your Bash PID made easy](./3-show_your_bash_pid_made_easy)** - Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash
- [x] **[4. To infinity and beyond](./4-to_infinity_and_beyond)** - Write a Bash script that displays To infinity and beyond indefinitely
- [x] **[5. Kill me now](./5-kill_me_now)** - We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this
- [x] **[6. Kill me now made easy](./6-kill_me_now_made_easy)** - Write a Bash script that kills 4-to_infinity_and_beyond process
- [x] **[7. Highlander](./7-highlander)** - Write a Bash script that displays to infinity and beyond indefinitely
- [x] **[8. Beheaded process](./8-beheaded_process)** - Write a Bash script that kills the process 7-highlander

### Advance :muscle:
- [x] **[9. Process and PID file](./100-process_and_pid_file)** - Write a Bash script that creates the file /var/run/holbertonscript.pid containing its PID
- [x] **[10. Manage my process](./101-manage_my_process)** - Write Bash (init) script 101-manage_my_process that manages manage_my_process. (both files need to be pushed to git)
- [x] **[11. Zombie](./102-zombie.c)** - Write a C program that creates 5 zombie processes.

## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)
