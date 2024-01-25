# configure nginx to work under stress

exec {'fix_nginx':
  # correct limit value
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin/:/bin/'],
}

# restart nginx

exec {'restart_nginx':
  command => '/usr/sbin/service nginx restart',
  path    => ['/usr/bin', '/bin'],
}
