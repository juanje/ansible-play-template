"""Role testing files using testinfra."""
import pytest


@pytest.mark.parametrize("bin_file", [
    ('/usr/bin/git')
])
def test_binary_file(host, bin_file):
    """Validate that the basic binary files are insttalled"""
    binary = host.file(bin_file)
    assert binary.exists
