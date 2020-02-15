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
    assert hblock.mode == "0o644"  # role default
