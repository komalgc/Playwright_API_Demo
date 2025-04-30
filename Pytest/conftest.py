import pytest

@pytest.fixture(scope="session")
def preSetupWork():
    print("this is my browser session")