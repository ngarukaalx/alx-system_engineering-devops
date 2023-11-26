#  using Puppet to make changes to our configuration file
file_line {'default':
ensure => present,
path   => '/ssh/config',
line   => ' IdentityFile ~/.ssh/school',
}

file_line {'pass iden':
ensure => present,
path   =>'/ssh/config',
line   => ' PasswordAuthentication no',
}
