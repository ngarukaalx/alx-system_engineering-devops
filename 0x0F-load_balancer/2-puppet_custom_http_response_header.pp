#  Add a custom HTTP header with Puppet

file {'/etc/nginx/sites-enabled/default':
  ensure  => present,
  content => "existing content\nX-Served-By \$HOSTNAME;
	\nmore existng content",
}
