# 0x19. Postmortem
## Issue Summary
On September 29, 2020, From 11:00 AM to 11:25 AM GMT-5, requests to the WordPress made web page resulted in `500 Internal Server Error` response messages. The issue affected 100% of traffic to this web site infrastructure. The root cause of this outage was a typographic error in the file `wp-settings.php`.
## Timeline 
- At 11:00 AM: The devops engineer sent a `GET` request to the server, receiving status code `500 Internal Server Error` response.
- At 11:05 AM: The devops engineer checked for all running processes on server with `ps -auxf`. finding a MySql and an Apache2 servers.
- At 11:10 AM: The devops engineer started tracing the syscalls called by the processes MySql and Apache2 with `strace -p <process_id>`. 
- At 11:14 AM: The devops engineer found a `ENOENT` (No such file or directory) error with the file `/var/www/html/wp-includes/class-wp-locale.phpp`, when traicing syscalls in Apache2 process.
- At 11:18 AM: The devops engineer searchs for the files containig the `class-wp-locale.phpp` pattern inside the Apache2 server root directory `/var/www/html/` with `grep class-wp-locale.phpp -r /var/www/html/` command, getting a match with the file `/var/www/html/wp-settings.php`.
- At 11:20 AM: The devops engineer found and fixed the typographic error, errasing the `p` at the end of `class-wp-locale.phpp`, inside the file `/var/www/html/wp-settings.php`.
- At 11:22 AM: The devops engineer sent a `GET` request again to the server, receiving status code `200 OK` response.
- At 11:25 AM: The dvops engineer wrote a puppet manifest to automate the error fixing.

## Root cause and resolution
The root cause was a typographic error in the file `/var/www/html/wp-settings.php`, the developer encharge of building the web site, added a `p`in the line `require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );` to the extension `.php` of the require file `/class-wp-locale.php`. Due the `class-wp-locale.phpp` file does not exist, when the system tried to check its status and open it, an `ENOENT` (No such file or directory) error was raising, causing an internal error in the Apache2 server, affecting the 100% of the traffic to this infrastructure.
## Corrective and preventative measures
