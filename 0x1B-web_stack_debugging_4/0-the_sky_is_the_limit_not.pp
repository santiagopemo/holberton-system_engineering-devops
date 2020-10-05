# increase the number of request nginx server can handle at time
exec { 'increase-ULIMIT':
  command => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 3000\"/g" /etc/default/nginx',
  path    => ['/bin']
}
exec { 'restart-nginx':
  command => 'service nginx restart',
  require => Exec['increase-ULIMIT']
}
