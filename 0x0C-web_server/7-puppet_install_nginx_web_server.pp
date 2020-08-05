# Install Nginx web server (w/ Puppet)
package { 'nginx':
  ensure => installed,
  name   => 'nginx',
}

service { 'nginx':
  ensure => running,
  enable => true,
  name   => 'nginx'
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Holberton School',
}

file_line { 'redirect':
  path  => '/etc/nginx/sites-available/default',
  after => 'listen 80 default_server;',
  line  => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}
