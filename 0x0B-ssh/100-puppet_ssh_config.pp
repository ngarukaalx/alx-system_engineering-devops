#  using Puppet to make changes to our configuration file
file {'/etc/ssh/ssh_config':
ensure  => present,
content => template('/home/vagrant/alx-system_engineering-devops/0x0B-ssh/ssh_config.erb'),
}
