import pytest
from functions.readFile import fileImport


def test_readFile():
    with pytest.raises(TypeError):
        readFile(20)
    with pytest.raises(TypeError):
        readFile(None)
    assert ([], []) == readFile("test")
    assert ([], []) == readFile("")
