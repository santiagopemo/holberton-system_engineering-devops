# Write 2-puppet_custom_http_response-header.pp so that it configures a brand new Ubuntu machine to the requirements asked in task 0

exec { 'update':
  command => 'sudo apt-get update -y',
  path    => ['/usr/bin', '/bin'],
}

package { 'nginx':
  ensure   => installed,
  name     => 'nginx'
  required => Exec['update'],
}

file_line { 'custom_header':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => "add_header X-Served-By $(hostname);",
  require => Package['nginx'],
}

exec { 'restart_nginx':
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
  require => Package['custom_header'],
}
