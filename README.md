Role Name
=========

Creates self-signed ssl certificates.

Requires that a CA and a certificate config are created. Example config and CA
creation script are found in the `bin` directory of this project.

Requirements
------------

None

Role Variables
--------------

| Name | Required | Default | Description |
| --- | --- | --- | --- |
|cert_owner | yes | root | Owner for the created files |
|cert_group | yes | root | Group for the created files |
|cert_ca_cert_src | yes | (none) | Local path to the CA cert |
|cert_ca_key_src | yes | (none) | Local path to the CA cert |
|cert_ca_conf_src | yes | (none) | Local path to the cert config |
|cert_ca_cert_name | yes | (none) | Name of the CA cert |
|cert_extension_name | yes | cert_ext | Cert extension name in the config file |
|cert_dest_directory | yes | (none) | Destination directory for the cert |
|cert_name | yes | (none) | Name of the certifiate to be created |

Dependencies
------------

None

Example Playbook
----------------

``` yaml
- name: Converge
  hosts: all
  pre_tasks:
  - name: Create test user
    user:
      name: testuser
      state: present
  - name: Create test directory
    file:
      path: /var/cache/ssl-test
      state: directory
  roles:
    - role: activatedio.sslcert
  vars:
    cert_ca_cert_src: ./certs/ca.crt
    cert_ca_key_src: ./certs/ca.key
    # TODO - Should change this name
    cert_ca_conf_src: ./certs/cert.conf
    cert_ca_cert_name: consul
    cert_dest_directory: /var/cache/ssl-test
    cert_name: servertest
    cert_owner: testuser
    cert_group: testuser
```

License
-------

MIT

Author Information
------------------

Ben Tomasini, Activated, Inc. - [btomasini@activated.io](mailto:btomasini@activated.io)
