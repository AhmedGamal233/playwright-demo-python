import pytest
import allure
from pages.Result import ResultPage
from pages.search import SearchPage
from playwright.sync_api import Page,sync_playwright,Playwright,Browser, BrowserType ,BrowserContext
from utils.Utilites import *

@pytest.fixture(scope="session")
def browser() -> Browser:
    # Start playwright
    browser: Playwright = sync_playwright().start()
    # Get browser information from config.py
    browser_info: dict = get_browser(browserName())
    # Get launcher attributes and set the browser as defined in broser_info
    launcher: BrowserType = getattr(browser, browser_info["browser"])
    # Launch browser
    return launcher.launch(
        headless=True, channel=browser_info.get("channel"),slow_mo=1000
    )

@pytest.fixture(scope="session")
def context(browser) -> BrowserContext:
    # Create new context
    context =browser.new_context()
    yield context
    
    # # Close context and browser
    context.close() 
    browser.close()


@pytest.fixture(scope="session")
def page(context) -> Page: 
    # Create new page
    page=context.new_page()
    global PAGE
    PAGE = page
    yield PAGE
    # Close page
    PAGE.close()


@pytest.fixture(scope='function')
def result_page(page: Page) -> ResultPage:
    return ResultPage(page)

@pytest.fixture(scope='function')
def search_page(page: Page) -> SearchPage:
    return SearchPage(page)

@pytest.fixture(scope='session')
def base_url():
    return base_Url()

PAGE = None

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport():
    outcome = yield
    test_result = outcome.get_result()

    if test_result.when in ["setup", "call"]:
        xfail = hasattr(test_result, 'wasxfail')
        if test_result.failed or (test_result.skipped and xfail):
            if PAGE:
                allure.attach(PAGE.screenshot(), name='screenshot', attachment_type=allure.attachment_type.PNG)
                allure.attach(PAGE.content(), name='html_source', attachment_type=allure.attachment_type.HTML)