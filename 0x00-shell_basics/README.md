# 0x00. Shell, basics
## Resources :books:

* [What Is The Shell?](./)
* [Navigation](./)
* [Looking Around](./)
* [A Guided Tour](./)
* [Manipulating Files](./)
* [Working With Commands](./)
* [Reading Man pages](./)
* [Keyboard shortcuts for Bash](./)
* [LTS](./)
* [Shebang](./)

## Learning Objectives :bulb:
* What does RTFM mean?
* What is a Shebang
* What is the shell
* What is the difference between a terminal and a shell
* What is the shell prompt
* How to use the history (the basics)
* What do the commands or built-ins cd, pwd, ls do
* How to navigate the filesystem
* What are the . and .. directories
* What is the working directory, how to print it and how to change it
* What is the root directory
* What is the home directory, and how to go there
* What is the difference between the root directory and the home directory of the user root
* What are the characteristics of hidden files and how to list them
* What does the command cd - do
* What do the commands ls, less, file do
* How do you use options and arguments with commands
* Understand the ls long format and how to display it
* A Guided Tour
* What does the ln command do
* What do you find in the most common/important directories
* What is a symbolic link
* What is a hard link
* What is the difference between a hard link and a symbolic link
* What do the commands cp, mv, rm, mkdir do
* What are wildcards and how do they work
* How to use wildcards
* What do type, which, help, man commands do
* What are the different kinds of commands
* What is an alias
* When do you use the command help instead of man
* How to read a man page
* What are man page sections
* What are the section numbers for User commands, System calls and Library functions
* Common shortcuts for Bash 

## Requirements :white_check_mark:
* Allowed editors: vi, vim, emacs
* All your scripts will be tested on Ubuntu 14.04 LTS
* All your scripts should be exactly two lines long ($ wc -l file should print 2)
* All your files should end with a new line (why?)
* The first line of all your files should be exactly #!/bin/bash
* A README.md file at the root of the holberton-system_engineering-devops repo, containing a description of the repository
* A README.md file, at the root of the folder of this project, describing what each script is doing
* You are not allowed to use backticks, &&, || or ;
* All your scripts must be executable. Use this command: chmod u+x file. We will see later what it means.

## Tasks :page_with_curl:
### Mandatory
- [x] **[0. Where am I?](./0-current_working_directory)** - Write a script that prints the absolute path name of the current working directory.
- [x] **[1. What’s in there?](./1-listit)** - Display the contents list of your current directory.
- [x] **[2. There is no place like home](./2-bring_me_home)** - Write a script that changes the working directory to the user’s home directory.
- [x] **[3. The long format](./3-listfiles)** - Display current directory contents in a long format
- [x] **[4. Hidden files](./4-listmorefiles)** - Display current directory contents, including hidden files (starting with .). Use the long format.
- [x] **[5. I love numbers](./5-listfilesdigitonly)** - Display current directory contents.
- [x] **[6. Welcome holberton](./6-firstdirectory)** - Create a script that creates a directory named holberton in the /tmp/ directory.
- [x] **[7. Betty in Holberton](./7-movethatfile)** - Move the file betty from /tmp/ to /tmp/holberton.
- [x] **[8. Bye bye Betty](./8-firstdelete)** - Delete the file betty.
- [x] **[9. Bye bye Holberton](./9-firstdirdeletion)** - Delete the directory holberton that is in the /tmp directory.
- [x] **[10. Back to the future](./10-back)** - Write a script that changes the working directory to the previous one.
- [x] **[11. Lists](./11-lists)** - Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
- [x] **[12. File type](./12-file_type)** - Write a script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.
- [x] **[13. We are symbols, and inhabit symbols](./13-symbolic_link)** - Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.
- [x] **[14. Copy HTML files](./14-copy_html)** - Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
- [x] **[15. Let’s move](./15-lets_move)** - Create a script that moves all files beginning with an uppercase letter to the directory /tmp/u.
- [x] **[16. Clean Emacs](./16-clean_emacs)** - Create a script that deletes all files in the current working directory that end with the character ~.
- [x] **[17. Tree](./17-tree)** - Create a script that creates the directories welcome/, welcome/to/ and welcome/to/holberton in the current directory.
### Advance :muscle:
- [x] **[18. Life is a series of commas, not periods](./18-commas)** - Write a command that lists all the files and directories of the current directory, separated by commas (,).
- [x] **[19. File type: Holberton](./holberton.mgc)** - Create a magic file holberton.mgc that can be used with the command file to detect Holberton data files. Holberton data files always contain the string HOLBERTON at offset 0.

## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)
