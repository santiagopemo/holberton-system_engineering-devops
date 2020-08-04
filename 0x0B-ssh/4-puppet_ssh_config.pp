
# Bash script that set up your client SSH configuration file so 
# that you can connect to a server without typing a password

file_line { 'no password':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => 'PasswordAuthentication',
}

file_line { 'private key at ~/.ssh/holberton':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
}
