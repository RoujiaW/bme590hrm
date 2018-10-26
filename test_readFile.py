import pytest
from readFile import fileImport

@pytest.mark.parametrize("input, output", [
    (test, NameError),
    ('test', FileNotFoundError),
    (1, ValueError),
])
def test_readFile(input, output):
    with pytest.raises(output):
        fileImport(input)
