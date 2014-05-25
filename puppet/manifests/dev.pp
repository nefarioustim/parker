$user = 'vagrant'

Exec {
    path => '/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin'
}

class { "user":
    username => $user,
    groupname => $user
}
