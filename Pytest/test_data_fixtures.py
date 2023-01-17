
import pytest
@pytest.mark.usefixtures("dataload")
class TestExamples2:

    def test_hello(self,dataload):
        print(dataload[0])