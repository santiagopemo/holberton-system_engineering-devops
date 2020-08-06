# Install Nginx web server (w/ Puppet)
package { 'nginx installed':
  ensure => installed,
  name   => 'nginx'
}

file { '/var/www/html/index.html':
  ensure  => present,
  path    => '/var/www/html/index.html',
  content => 'Holberton School'
}

file_line { 'redirection':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;'
}

service { 'nginx':
  ensure     => running,
  require    => Package['nginx'],
  hasrestart => true
}
