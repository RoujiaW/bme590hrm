import pytest
from readFile import fileImport


def test_fileImport():
    with pytest.raises(TypeError):
        fileImport(20)
    with pytest.raises(TypeError):
        fileImport(None)
    assert ([], []) == fileImport("test")
    assert ([], []) == fileImport("")
