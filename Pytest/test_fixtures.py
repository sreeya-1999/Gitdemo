import pytest
@pytest.mark.usefixtures("setup")
class TestExamples:

    def test_hello(self):
        print("i am wat?")




    def test_fixture_demo(self):
        print("joy")

    def test_hi(self):
        print("hiiiiii")


def test_crossbrowser(CrossBrowser):
    print(CrossBrowser)





