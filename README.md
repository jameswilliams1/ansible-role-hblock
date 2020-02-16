hblock
=========

This role installs and then runs hBlock on Linux. It will backup then append to `/etc/hosts` in order to block adverts and trackers system-wide. Unlike the original hBlock script, your existing changes to the hosts file will be preserved.

**Note:** this is a work in progress and currently only supports a few settings for hBlock. In the future options will be added to provide a more customised setup, as well as systemd timer support for updating block lists. Although every effort has been taken to prevent bugs, this role **will** modify your systems hosts file. Usage is entirely at your own risk.

Requirements
------------

- Either curl or wget must be available on the host machine in order to run hBlock
- A POSIX compatible shell is required on the host

Role Variables
--------------
Some configuration is left as an option to the user, but generally only the version should be changed.  
**NB:** setting `hblock_root_only: false` will allow anyone to modify the hosts file using hBlock. It is not recommended.
```yaml
hblock_version:  Version of hBlock script to download
hblock_download_checksum:  Hash of hBlock script prefixed with hash type (see example)
hblock_install_dir:  Directory to install hBlock to
hblock_root_only:  Whether to restrict usage of hBlock to root
hblock_output_file: File to write the blocklist to (default /etc/hosts)
```

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: all
  roles:
     - hblock
  vars:
    hblock_version: '2.1.4'
    hblock_download_checksum: 'sha256:a379434ebd58b0b976244d568a299318aa24e7be8d67\
    95b5f8224bad3f4b44b8'
    hblock_install_dir: /usr/local/bin  # Generally no reason to change this
    hblock_root_only: false  # WARNING If false, allows non root users to modify hosts file using hBlock
```

License
-------

MIT

Author Information
------------------

James Williams  
[https://github.com/jameswilliams1/](https://github.com/jameswilliams1/ "GitHub Page")
