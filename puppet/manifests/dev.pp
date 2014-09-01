$user = 'vagrant'
$project = 'parker'

Exec {
    path => '/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin'
}

include core-env

class { "user":
    name        => $user,
    groupname   => $user,
    projectpath => "/home/${user}/${project}"
}

include libxml

include python
include python::virtualenv
include python::supervisor

include redis
