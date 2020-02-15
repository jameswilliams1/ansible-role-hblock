hblock
=========

This role installs hBlock on Linux. It will append to the hosts file (/etc/hosts by default) in order to block adverts and trackers system-wide.

**Note:** this is a work in progress and currently only supports a few settings for hBlock. In the future options will be added to provide a more customised setup as well as systemd timer support.

Requirements
------------

- Either curl or wget must be available on the host to run hBlock

Role Variables
--------------

TODO

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: all
  roles:
     - hblock
```

License
-------

MIT

Author Information
------------------

James Williams
[https://github.com/jameswilliams1/](https://github.com/jameswilliams1/ "GitHub Page")
