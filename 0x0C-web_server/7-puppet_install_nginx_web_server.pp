# Install Nginx web server (w/ Puppet)
exec { 'Install Nginx':
  command => 'sudo apt-get install nginx -y',
  path    => ['/usr/bin', '/bin'],
}

file { '/var/www/html/index.html':
  content => 'Holberton School',
}

file_line { 'title':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  after    => 'server_name _;',
  line     => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  multiple => true
}

exec { 'Stop Nginx':
  require => Exec['Install Nginx'],
  command => 'sudo service nginx stop',
  path    => ['/usr/bin', '/bin', '/usr/sbin'],
}

exec { 'Start Nginx':
  require => Exec['Stop Nginx'],
  command => 'sudo service nginx start',
  path    => ['/usr/bin', '/bin', '/usr/sbin'],
}
