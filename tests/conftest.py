import os

import allure
import pytest
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser

from online_market.models.pages.cart_menu import cart_menu
from online_market.models.pages.display_page import display_page
from online_market.models.pages.displays_page import displays_page
from online_market.utils import attach

load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASS')
    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
        options=options
    )

    browser.config.driver = driver
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = "https://www.online-market.by"

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture(scope='function')
def open_first_display():
    displays_page.open()
    displays_page.open_first_display()

    displays_page.should_open_first_display()


@pytest.fixture(scope='function')
def add_first_display_in_cart():
    displays_page.open()
    cart_menu.add_first_product()

    cart_menu.should_product()


@pytest.fixture(scope='function')
def add_first_display_to_compare(open_first_display):
    display_page.add_display_to_compare()

    display_page.should_display_to_compare()


@pytest.fixture(scope='function')
def add_first_display_in_favorites(open_first_display):
    display_page.add_display_in_favorites()

    display_page.should_display_in_favorites()
