hblock
=========

This role installs hBlock on Linux. It will overwrite a specified host file (/etc/hosts by default) in order to block adverts and trackers system-wide.

**Note:** this is a work in progress and currently only supports the default settings for hBlock. In the future options will be added to provide a more custom setup and also systemd timer support.

Requirements
------------

None.

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
