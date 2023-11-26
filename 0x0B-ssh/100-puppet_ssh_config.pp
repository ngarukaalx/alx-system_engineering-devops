#  using Puppet to make changes to our configuration file
file {'/home/vagrant/.ssh/config':
ensure  => present,
content => template('/home/vagrant/alx-system_engineering-devops/0x0B-ssh/ssh_config.erb'),
}
