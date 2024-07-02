# kill process killmenow but let programmer stay

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
