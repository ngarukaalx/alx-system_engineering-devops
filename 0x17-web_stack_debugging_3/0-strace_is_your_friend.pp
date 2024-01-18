# edit file to fix Apache returning a 500 error

$correct_file = '/var/www/html/wp-settings.php'
exec { 'edit_file':
  command => "sed -i 's/phpp/php/g' ${correct_file}",
  path    => ['/bin', '/usr/bin'],
}
