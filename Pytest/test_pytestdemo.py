import pytest
#to run the test on command use pytest and file name
#to run particular test in file use pytest filename::testname -s
#to skip any test use @pytest.mark.skip
#to tag any test use @pytest.mark.smoke and run pytest -m smoke

@pytest.fixture(scope="module")
def prework():
    print("this is the prework")
    return "true"

@pytest.fixture(scope="function")
def pretest():
    print("this is my pretest")
    yield #to pause , execute the test and  comeback n continue
    print("this is teardown")



def test_initialtest(prework,pretest):
    print("this is my first test")
    assert prework == "true"

def test_randomcheck(prework, pretest):
    print("this is randomcheck")



def test_secondtest(preSetupWork):
    print("this is my second test")
