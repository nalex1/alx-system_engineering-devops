# to create a file in /tmp by puppet all is possible

file { 'wonder':
  path    =>  '/tmp/school',
  mode    =>  '0744',
  owner   =>  'www-data',
  group   =>  'www-data',
  content =>  'I love Puppet',
}
