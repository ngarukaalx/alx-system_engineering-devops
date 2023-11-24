#  install flask from pip3.
package {'Werkzeug':
ensure   => '2.2.2',
provider => 'pip3',
}
