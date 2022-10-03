import pytest
from selene.support.shared import browser
import allure


@pytest.fixture(scope='function', autouse=True)
def browser_configs():
    browser.config.window_width = 1400
    browser.config.window_height = 1600
    browser.config.browser_name = 'chrome'


@pytest.fixture()
def open_and_close_form():
    browser.open_url("https://demoqa.com/automation-practice-form")
    yield
    browser.element("#closeLargeModal").double_click()
    browser.close()
