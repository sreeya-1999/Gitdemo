import pytest


@pytest.fixture(scope="class")
def setup():
    print("i am executing 1st")

    yield
    print("i m last")


@pytest.fixture()
def dataload():
    print("to pass data")
    return ["https://rahulshettyacademy.com/dropdownsPractise/"]


@pytest.fixture(params=[("chrome","sreeya"),("firefox","neeraj"),("IE","bhooms")])
def CrossBrowser(request):
    return request.param
