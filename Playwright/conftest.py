import pytest


@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param


@pytest.fixture(scope="session")
def browserInstance(playwright,request):
    browser_name = request.config.getoption("browser_name")
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

