# 0x19. Postmortem
## Issue Summary
On September 29, 2020, From 11:00 AM to 11:25 AM GMT-5, requests to the WordPress made web page resulted in `500 Internal Server Error` response messages. The issue affected 100% of traffic to this web site infrastructure. The root cause of this outage was a typographic error in the file `wp-settings.php`, for unknown reasons, the engineer in charge of developing the page entered an extra `p`.
## Timeline 
- At 11:00 AM: The devops engineer sent a `GET` request to the server, receiving status code `500 Internal Server Error` response.
- At 11:05 AM: The devops engineer checked for all running processes on server with `ps -auxf`. finding a MySql and an Apache2 servers.
- At 11:10 AM: The devops engineer started tracing the syscalls called by the processes MySql and Apache2 with `strace -p <process_id>`. 
- At 11:14 AM: The devops engineer found a `ENOENT` (No such file or directory) error with the file `/var/www/html/wp-includes/class-wp-locale.phpp`, when traicing syscalls after sent a `GET` request to the server in Apache2 process.
- At 11:18 AM: The devops engineer searchs for the files containig the `class-wp-locale.phpp` pattern inside the Apache2 server root directory `/var/www/html/` with `grep class-wp-locale.phpp -r /var/www/html/` command, getting a match with the file `/var/www/html/wp-settings.php`.
- At 11:20 AM: The devops engineer found and fixed the typographic error, errasing the `p` at the end of `class-wp-locale.phpp`, inside the file `/var/www/html/wp-settings.php`.
- At 11:22 AM: The devops engineer sent a `GET` request again to the server, receiving status code `200 OK` response.
- At 11:25 AM: The devops engineer wrote a puppet manifest to automate the error fixing.
- At 11:30 AM: The devops engineer sent a message to the developer encharge of building the web site to warn him about his mistake.
- At 11:32 AM: The devops engineer recive a photo from the developer encharge of building the web site: 
  
![](https://funnypics.photosandpictures.net/main.php?g2_view=core.DownloadItem&g2_itemId=6761&g2_serialNumber=1)

## Root cause and resolution
It seems that when the developer was in the bathroom, his cat took advantage of and modified several of the files he was working on in retaliation for not having petted him all day. Although it was able to correct most of the files, `wp-settings.php` was missing.  
The root cause was a typographic error in the file `/var/www/html/wp-settings.php`, the developer´s kitten, added a `p`in the line `require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );` to the extension (`.phpp`) of the require file `/class-wp-locale.php`. Due the `class-wp-locale.phpp` file does not exist, when the system tried to check its status and open it, an `ENOENT` (No such file or directory) error was raising, causing an internal error in the Apache2 server, affecting the 100% of the traffic to this infrastructure. The solution was simply to delete the extra `p`, and generate a puppet manifest to automate the solution of this typographic error.

## Corrective and preventative measures
This type of problem can be prevented, using a server only for development, and/or another for testing in which all the necessary tests can be carried out, prior to deployment. It is also important to implement a quality control department, which allocates at least 30% of the project development time for testing, to ensure that the software can perform everything expected correctly, even when the functionality to be validated is already for more known, since each project has variables that make them different.  
Quality assurance is a primary stage in a software develpment project, since at this stage it is possible to validate all the break points and crucial points in the operation of a given business and towards which the software is directed.




