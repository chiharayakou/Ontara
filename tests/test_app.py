from ontara import __version__

def test_version_is_valid() -> None:
    assert __version__ == "0.0.1.dev0"