import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_configs():
    browser.config.window_width = 1400
    browser.config.window_height = 1600
    browser.config.browser_name = 'chrome'
    browser.config.base_url = "https://demoqa.com"


@pytest.fixture()
def open_and_close_form():
    browser.open("/automation-practice-form")
    yield
    browser.element("#closeLargeModal").double_click()
    browser.close()
