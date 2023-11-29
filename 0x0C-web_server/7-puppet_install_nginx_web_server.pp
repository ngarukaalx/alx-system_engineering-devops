# Installs nginx and configures

package {'nginx':
  ensure => 'installed',
}

# Helllo world index.html
file {'/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
}

# Redirect 301, listent port 80
file_line {'nginx_redirect':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://madukaonline.co.ke/ permanent;',
}

service { 'nginx':
  ensure  => 'running',
  require => package['nginx']
}
