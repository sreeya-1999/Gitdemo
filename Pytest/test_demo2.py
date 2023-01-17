import pytest


def test_third():
    mssg="how are you?"
    assert 'how' in mssg,'this is wrong'
@pytest.mark.light
@pytest.mark.skip
def test_all():
    print("you are amazing")