# 0x01. Shell, permissions
## Resources :books:

* [Permissions](https://intranet.hbtn.io/rltoken/5uUsOHrMbVBOpZFteNyBLg)

## Learning Objectives :bulb:
* What do the commands chmod, sudo, su, chown, chgrp do
* Linux file permissions
* How to represent each of the three sets of permissions (owner, group, and other) as a single digit
* How to change permissions, owner and group of a file
* Why cant a normal user chown a file
* How to run a command with root privileges
* How to change user ID or become superuser
* How to create a user
* How to create a group
* How to print real and effective user and group IDs
* How to print the groups a user is in
* How to print the effective userid

## Requirements :white_check_mark:

* Allowed editors: vi, vim, emacs
* All your scripts will be tested on Ubuntu 14.04 LTS
* All your scripts should be exactly two lines long ($ wc -l file should print 2)
* All your files should end with a new line (why?)
* The first line of all your files should be exactly #!/bin/bash
* A README.md file, at the root of the folder of the project, describing what each script is doing
* You are not allowed to use backticks, &&, || or ;
* All your files must be executable

## Tasks :page_with_curl:
### Mandatory
- [x] **[0. My name is Betty](./0-iam_betty)** - Create a script that changes your user ID to betty.
- [x] **[1. Who am I](./1-who_am_i)** - Write a script that prints the effective userid of the current user.
- [x] **[2. Groups](./2-groups)** - Write a script that prints all the groups the current user is part of.
- [x] **[3. New owner](./3-new_owner)** - Write a script that changes the owner of the file hello to the user betty.
- [x] **[4. Empty!](./4-empty)** - Write a script that creates an empty file called hello.
- [x] **[5. Execute](./5-execute)** - Write a script that adds execute permission to the owner of the file hello.
- [x] **[6. Multiple permissions](./6-multiple_permissions)** - Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
- [x] **[7. Everybody](./7-everybody)** - Write a script that adds execution permission to the owner, the group owner and the other users, to the file hello
- [x] **[8. James Bond](./8-James_Bond)** - Write a script that sets the permission to the file hello as follows:
- [x] **[9. John Doe](./9-John_Doe)** - Write a script that sets the mode of the file hello
- [x] **[10. Look in the mirror](./10-mirror_permissions)** - Write a script that sets the mode of the file hello the same as olleh’s mode.
- [x] **[11. Directories](./11-directories_permissions)** - Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.
- [x] **[12. More directories](./12-directory_permissions)** - Create a script that creates a directory called dir_holberton with permissions 751 in the working directory.
- [x] **[13. Change group](./13-change_group)** - Write a script that changes the group owner to holberton for the file hello
- [x] **[14. Owner and group](./14-change_owner_and_group)** - Write a script that changes the owner to betty and the group owner to holberton for all the files and directories in the working directory.
- [x] **[15. Symbolic links](./15-symbolic_link_permissions)** - Write a script that changes the owner and the group owner of the file _hello to betty and holberton respectively.
- [x] **[16. If only](./16-if_only)** - Write a script that changes the owner of the file hello to betty only if it is owned by the user guillaume.
### Advance :muscle:
- [x] **[17. Star Wars](./100-Star_Wars)** - Write a script that will play the StarWars IV episode in the terminal.
- [ ] **[18. RTFM](./101-man_holberton)** - Create a man page that looks exactly like this one and passes all checks.

## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)
