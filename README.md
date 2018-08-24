Role Name
=========

Creates self signed ssl-certificates

Requirements
------------

None

Role Variables
--------------

| Name | Default | Description |
| --- | --- | --- |
|cert_owner | root | Owner for the created files |
|cert_group | root | Group for the created files |

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: ansible-activated-openssl, x: 42 }

License
-------

MIT

Author Information
------------------

Ben Tomasini, Activated, Inc. - [btomasini@activated.io](mailto:btomasini@activated.io)
