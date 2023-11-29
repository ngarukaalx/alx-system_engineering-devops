#  using Puppet to make changes to our configuration file
file {'/etc/ssh/ssh_config':
ensure  => present,
content => "
Host *
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
