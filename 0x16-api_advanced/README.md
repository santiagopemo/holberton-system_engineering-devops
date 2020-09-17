# 0x16. API advanced

## Resources :books:
### Read or watch:
* [Reddit API Documentation]()
* [Query String]()

## Learning Objectives :bulb:
* At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
* How to read API documentation to find the endpoints you’re looking for
* How to use an API with pagination
* How to parse JSON results from an API
* How to make a recursive API call
* How to sort a dictionary by value
## Requirements :white_check_mark:
### General
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* Libraries imported in your Python files must be organized in alphabetical order
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* You must use the Requests module for sending HTTP requests to the Reddit API
## Tasks
### Mandatory :page_with_curl:
- [x] **[0. How many subs?](./0-subs.py)** - Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0
- [x] **[1. Top Ten](./1-top_ten.py)** - Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit
- [x] **[2. Recurse it!](./2-recurse.py)** - Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None
### Advance :muscle:
- [x] **[3. Count it!](./100-count.py)** - Write a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not)
## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)
