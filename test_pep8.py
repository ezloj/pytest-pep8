
pytest_plugins = "pytester",

def test_simple(testdir):
    testdir.makepyfile("""
        class AClass:
            pass
            
            
            
        # too many spaces
    """)
    result = testdir.runpytest("--pep8")
    result.stdout.fnmatch_lines([
        "*W293*",
    ])
    assert result.ret != 0

def test_ok_verbose(testdir):
    p = testdir.makepyfile("""
        class AClass:
            pass
    """)
    p = p.write(p.read() + "\n")
    result = testdir.runpytest("--pep8", "--verbose")
    result.stdout.fnmatch_lines([
        "*test_ok_verbose*PEP8-check*",
    ])
    assert result.ret == 0
