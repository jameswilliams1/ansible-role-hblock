import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_hblock_script_installed(host):
    hblock = host.file("/usr/local/bin/hblock")
    assert hblock.exists
    assert hblock.is_file
    assert hblock.user == "root"
    assert hblock.group == "root"
    assert oct(hblock.mode) == "0o744"  # role default


def test_role_does_not_destroy_existing_hosts_file(host):
    message = "# File not overwritten"  # added as a test before running role
    hosts_file = host.file("/etc/hosts")
    assert hosts_file.content_string.split("\n")[0] == message  # first line
