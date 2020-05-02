# 0x03. Shell, init files, variables and expansions
## Resources :books:

* [Expansions](./)
* [Shell Arithmetic](./)
* [Variables](./)
* [Shell initialization files](./)
* [The alias Command](./)
* [Technical Writing](./)

## Learning Objectives :bulb:
* What happens when you type $ ls -l *.txt
* Shell Initialization Files
* What are the /etc/profile file and the /etc/profile.d directory
* What is the ~/.bashrc file
* Variables
* What is the difference between a local and a global variable
* What is a reserved variable
* How to create, update and delete shell variables
* What are the roles of the following reserved variables: HOME, PATH, PS1
* What are special parameters
* What is the special parameter $??
* Expansions
* What is expansion and how to use them
* What is the difference between single and double quotes and how to use them properly
* How to do command substitution with $() and backticks
* Shell Arithmetic
* How to perform arithmetic operations with the shell
* The alias Command
* How to create an alias
* How to list aliases
* How to temporarily disable an alias
* Other help pages
* How to execute commands from a file in the current shell

## Requirements :white_check_mark:
* Allowed editors: vi, vim, emacs
* All your scripts will be tested on Ubuntu 14.04 LTS
* All your scripts should be exactly two lines long ($ wc -l file should print 2)
* All your files should end with a new line (why?)
* The first line of all your files should be exactly #!/bin/bash
* A README.md file, at the root of the folder of the project, describing what each script is doing
* You are not allowed to use &&, || or ;
* You are not allowed to use bc, sed or awk
* All your files must be executable
## Tasks :page_with_curl:
### Mandatory
- [x] **[0. <o>](./0-alias)** - Create a script that creates an alias.
- [x] **[1. Hello you](./1-hello_you)** - Create a script that prints hello user, where user is the current Linux user.
- [x] **[2. The path to success is to take massive, determined action](./2-path)** - Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program.
- [x] **[3. If the path be beautiful, let us not ask where it leads](./3-paths)** - Create a script that counts the number of directories in the PATH.
- [x] **[4. Global variables](./4-global_variables)** - Create a script that lists environment variables.
- [x] **[5. Local variables](./5-local_variables)** - Create a script that lists all local variables and environment variables, and functions.
- [x] **[6. Local variable](./6-create_local_variable)** - Create a script that creates a new local variable.
- [x] **[7. Global variable](./7-create_global_variable)** - Create a script that creates a new global variable.
- [x] **[8. Every addition to true knowledge is an addition to human power](./8-true_knowledge)** - Write a script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.
- [x] **[9. Divide and rule](./9-divide_and_rule)** - Write a script that prints the result of POWER divided by DIVIDE, followed by a new line.
- [x] **[10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath](./10-love_exponent_breath)** - Write a script that displays the result of BREATH to the power LOVE
- [x] **[11. There are 10 types of people in the world -- Those who understand binary, and those who don't](./11-binary_to_decimal)** - Write a script that converts a number from base 2 to base 10.
- [x] **[12. Combination](./12-combinations)** - Create a script that prints all possible combinations of two letters, except oo.
- [x] **[13. Floats](./13-print_float)** - Write a script that prints a number with two decimal places.
- [x] **[14. Decimal to Hexadecimal](./14-decimal_to_hexadecimal)** - Write a script that converts a number from base 10 to base 16.
### Advance :muscle:
- [x] **[17. Everyone is a proponent of strong encryption](./100-rot13)** - Write a script that encodes and decodes text using the rot13 encryption. Assume ASCII.
- [x] **[18. The eggs of the brood need to be an odd number](./101-odd)** - Write a script that prints every other line from the input, starting with the first line.
- [x] **[19. I'm an instant star. Just add water and stir.](./102-water_and_stir)** - Write a shell script that adds the two numbers stored in the environment variables WATER and STIR and prints the result.

## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)
