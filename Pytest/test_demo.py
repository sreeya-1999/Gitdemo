import pytest


@pytest.mark.light
def test_first():
    print("hello")
def test_second():
    print("goodmorning")
def test_crossbrowser(CrossBrowser):
    print(CrossBrowser)