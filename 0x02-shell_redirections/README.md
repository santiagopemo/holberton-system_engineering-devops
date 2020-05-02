# 0x02. Shell, I/O Redirections and filters
## Resources :books:

* [Shell, I/O Redirection](https://intranet.hbtn.io/rltoken/Kwe7oA6N7iWf8kfnteJLrA)
* [Special Characters](https://intranet.hbtn.io/rltoken/6G_Cu3hczr_SdaSzlunjZg)

## Learning Objectives :bulb:
* What do the commands head, tail, find, wc, sort, uniq, grep, tr do
* How to redirect standard output to a file
* How to get standard input from a file instead of the keyboard
* How to send the output from one program to the input of another program
* How to combine commands and filters with redirections
* Special Characters
* What are special characters
* Understand what do the white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde and how and when to use them
* Other Man Pages
* How to display a line of text
* How to concatenate files and print on the standard output
* How to reverse a string
* How to remove sections from each line of files
* What is the /etc/passwd file and what is its format
* What is the /etc/shadow file and what is its format

## Requirements :white_check_mark:
* Allowed editors: vi, vim, emacs
* All your scripts will be tested on Ubuntu 14.04 LTS
* All your scripts should be exactly two lines long ($ wc -l file should print 2)
* All your files should end with a new line (why?)
* The first line of all your files should be exactly #!/bin/bash
* A README.md file, at the root of the folder of the project, describing what each script is doing
* You are not allowed to use backticks, &&, || or ;
* All your files must be executable
* You are not allowed to use sed or awk

## Tasks :page_with_curl:
### Mandatory
- [x] **[0. Hello World](./0-hello_world)** - Write a script that prints “Hello, World”, followed by a new line to the standard output.
- [x] **[1. Confused smiley](./1-confused_smiley)** - Write a script that displays a confused smiley "(Ôo)'.
- [x] **[2. Let's display a file](./2-hellofile)** - Display the content of the /etc/passwd file.
- [x] **[3. What about 2?](./3-twofiles)** - Display the content of /etc/passwd and /etc/hosts
- [x] **[4. Last lines of a file](./4-lastlines)** - Display the last 10 lines of /etc/passwd
- [x] **[5. I'd prefer the first ones actually](./5-firstlines)** - Display the first 10 lines of /etc/passwd
- [x] **[6. Line #2](./6-third_line)** - Write a script that displays the third line of the file iacta.
- [x] **[7. It is a good file that cuts iron without making a noise](./7-file)** - Write a shell script that creates a file named exactly \*\\'"Holberton School"\'\\*$\?\*\*\*\*\*:) containing the text Holberton School ending by a new line.
- [x] **[8. Save current state of directory](./8-cwd_state)** - Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.
- [x] **[9. Duplicate last line](./9-duplicate_last_line)** - Write a script that duplicates the last line of the file iacta
- [x] **[10. No more javascript](./10-no_more_js)** - Write a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.
- [x] **[11. Don't just count your directories, make your directories count](./11-directories)** - Write a script that counts the number of directories and sub-directories in the current directory.
- [x] **[12. What’s new](./12-newest_files)** - Create a script that displays the 10 newest files in the current directory.
- [x] **[13. Being unique is better than being perfect](./13-unique)** - Create a script that takes a list of words as input and prints only words that appear exactly once.
- [x] **[14. It must be in that file](./14-findthatword)** - Display lines containing the pattern “root” from the file /etc/passwd
- [x] **[15. Count that word](./15-countthatword)** - Display the number of lines that contain the pattern “bin” in the file /etc/passwd
- [x] **[16. What's next?](./16-whatsnext)** - Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.
- [x] **[17. I hate bins](./17-hidethisword)** - Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.
- [x] **[18. Letters only please](./18-letteronly)** - Display all lines of the file /etc/ssh/sshd_config starting with a letter.
- [x] **[19. A to Z](./19-AZ)** - Replace all characters A and c from input to Z and e respectively.
- [x] **[20. Without C, you would live in hiago](./20-hiago)** - Create a script that removes all letters c and C from input.
- [x] **[21. esreveR](./21-reverse)** - Write a script that reverse its input.
- [x] **[22. DJ Cut Killer](./22-users_and_homes)** - Write a script that displays all users and their home directories, sorted by users.
### Advance :muscle:
- [x] **[23. Empty casks make the most noise](./100-empty_casks)** - Write a command that finds all empty files and directories in the current directory and all sub-directories.
- [x] **[24. A gif is worth ten thousand words](./101-gifs)** - Write a script that lists all the files with a .gif extension in the current directory and all its sub-directories.
- [x] **[25. Acrostic](./102-acrostic)** - An acrostic is a poem (or other form of writing) in which the first letter (or syllable, or word) of each line (or paragraph, or other recurring feature in the text) spells out a word, message or the alphabet. The word comes from the French acrostiche from post-classical Latin acrostichis). As a form of constrained writing, an acrostic can be used as a mnemonic device to aid memory retrieval. Read more.
- [x] **[26. The biggest fan](./103-the_biggest_fan)** - Write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.

## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)
