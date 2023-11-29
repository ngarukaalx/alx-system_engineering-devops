# Installs nginx and configures with requirements

package {'nginx':
  ensure => installed,
}

exec {'update':
  command  => 'apt-get update',
  provider => shell,
  notify   => Exec['install'],
}

exec {'install':
  command  => 'apt-get -y install nginx',
  provider => shell,
  notify   => Exec['configure_nginx'],
}

# Helllo world index.html
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Redirect 301, listent port 80
exec { 'configure_nginx':
  command  => '/usr/bin/sedsed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/madukaonline.co.ke\/ permanent/" /etc/nginx/sites-enabled/default',
  notify   => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command  => 'service nginx restart',
  provider => shell,
}
