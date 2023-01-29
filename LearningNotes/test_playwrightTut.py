# # '''
# # Inside this project, create a Python virtual environment using the venv module to manage dependency packages locally:
# # python3 -m venv venv
# # After creating a virtual environment, you must "activate" it.
# # source venv/bin/activate  ot at windows  venv\Scripts\activate.bat
# # pip3 install playwright
# # pip3 install pytest
# # pip3 install pytest-playwright
# # You can check all installed packages using pip3 freeze (store all dependencies in requirments.txt and just run this command to use project in other machine => pip3 install -r requirements.txt)

# # The playwright install command installs the latest versions of the three browsers that Playwright supports: Chromium, Firefox, and WebKit:

# # playwright install

# # mkdir tests
# # touch tests/test_search.py
# # '''


# # Before we can automate interactions using Playwright's API, we must first understand how Playwright interacts with browsers. There are three main layers to automation: browsers, browser contexts, and pages:

# #1- A browser is a single instance of a web browser. Playwright will automatically launch a browser instance specified by code or by inputs.
# # Typically, this is either the Chromium, Firefox, or WebKit instance installed via playwright install, 
# # but it may also be other browsers installed on your local machine.

# #2- A browser context is an isolated incognito-alike session within a browser instance.
# # They are fast and cheap to create. One browser may have multiple browser contexts. 
# # *****The recommended practice is for all tests to share one browser instance but for each test to have its own browser context.

# #3- A page is a single tab or window within a browser context. A browser context may have multiple pages.
# # Typically, an individual test should interact with only one page.

# from playwright.sync_api import sync_playwright,Page,expect,Keyboard

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()

# # The browser fixture provides the browser instance launched by Playwright.
# # The context fixture provides a new browser context for a test.
# # The page fixture provides a new browser page for a test.

# def test_basic_duckduckgo_search(page: Page):
#     # Given the DuckDuckGo home page is displayed
#     page.goto('https://www.duckduckgo.com', wait_until='networkidle')
#     # When the user searches for a phrase
#     # to enter text into this input element, we must use Locator's fill method.
#     page.locator('#search_form_input_homepage').fill('panda')
#     sync_playwright.selectors.set_test_id_attribute('id') #or whatever the name of id in node data-id /data-pw ..etc
#     page.locator('#search_button_homepage').click()
#     # Then the search result query is the phrase
#     # locator is a method that returns a Locator object for the target element. A Locator object can make many of the same calls as a page, like clicking and getting text. However, it can also make calls for explicit waiting and calls that target multiple elements.
#     # a[data-testid="result-title-a"] is the selector for the result links.
#     # nth(4) is an N-th element fetcher. N-th element fetchers are zero-indexed and may be appended to any selector. In this call, it will fetch the fifth result link element.
#     # wait_for is a method that will wait for the target element to be visible.
#     page.locator('a[data-testid="result-title-a"]').nth(4).wait_for()
#     titles = page.locator('a[data-testid="result-title-a"]').all_text_contents()
#     matches = [t for t in titles if 'panda' in t.lower()]
#     # This is a Python list comprehension. Basically, it filters titles for elements that contain the search phrase.
#     # If the lowercase version of a title contains the search phrase, then it is added to matches. Otherwise, it is omitted.
#     assert len(matches) > 0
#     # And the search result links pertain to the phrase
#     # And the search result title contains the phrase
#     expect(page).to_have_title('panda at DuckDuckGo')
#     # while(not page.get_by_text("More results").is_visible()):
#     #     page.mouse.wheel(0, 15000)
#     #     if page.get_by_text("More results").is_visible:
#     #         break
#     # page.get_by_text("More results").click()
#     while(not page.locator("(//a[contains(@href,'twitter')])[last()]").is_visible()):
#         #mouse.wheel(x, y) x horizontall scroll ,y vertical
#         # page.mouse.wheel(0, 5000)
#         page.keyboard.down('PageDown') #also works
#         if page.locator("(//a[contains(@href,'twitter')])[last()]").is_visible:
#             break
#     page.locator("(//a[contains(@href,'twitter')])[last()]").click()



# # All the Playwright calls with pytest-playwright use the synchronous API instead of the async API. 
# # The browser fixture has session scope, meaning all tests will share one browser instance. 
# # The context and page fixtures have function scope, meaning each test gets new ones. Typically, a test will only need to call the page fixture directly.
# # These fixtures will also automatically clean up everything after testing is complete. You do not need to explicitly close the browser.

# # Playwright supports both synchronous and asynchronous calls for Python. Synchronous calls are sufficient for almost all test automation needs.
# # Asynchronous calls could be useful for other types of automation, such as web scraping.


# # python3 -m pytest tests --headed --slowmo 1000

# # This invocation has two new arguments. The first one is --headed. By default, Playwright runs tests in headless mode,
# # in which the browser is not visibly rendered. Headless mode is faster than headed mode and thus ideal for "real" testing (like in CI).
# # However, headed mode is better when developing tests so that you can see what is happening.


# # Playwright supports the following types of selectors:

# # Text
# # CSS
# # XPath
# # N-th element
# # React
# # Vue
# # ID attributes
# # Text and CSS selectors also pierce the Shadow DOM by default!

# from pages.search import SearchPage
# from pages.Result import ResultPage

# def test_basic_duckduckgo_search(page: Page) -> None:
#     search_page = SearchPage(page)
#     result_page = ResultPage(page)
    
#     # Given the DuckDuckGo home page is displayed
#     search_page.load()

#     # When the user searches for a phrase
#     search_page.search('panda')

#     # Then the search result query is the phrase
#     expect(result_page.search_input).to_have_value('panda')

#     # And the search result links pertain to the phrase
#     assert result_page.result_link_titles_contain_phrase('panda')

#     # And the search result title contains the phrase
#     expect(page).to_have_title('panda at DuckDuckGo')
    
    
#Final shape of POM with base test
import pytest
from pages.Result import ResultPage
from pages.search import SearchPage
from utils.Utilites import *
from playwright.sync_api import sync_playwright,expect, Page


@pytest.mark.US
@pytest.mark.parametrize("searches,rest_of_search",read_test_data_from_csv_multi_col())
def test_basic(
    searches,
    rest_of_search,
    base_url,
    page: Page,
    search_page: SearchPage,
    result_page: ResultPage):
    
    # Given the DuckDuckGo home page is displayed
    search_page.load(base_url)
    
    # When the user searches for a phrase
    search_page.search(f'{searches}')

    # Then the search result query is the phrase
    page.wait_for_load_state()
    expect(result_page.search_input).to_have_value(f'{searches}')

    # And the search result links pertain to the phrase
    assert result_page.result_link_titles_contain_phrase(f'{searches}')

    # And the search result title contains the phrase
    expect(page).to_have_title(f'{searches}{rest_of_search}')
    
    result_page.scrollToTwitter()
    result_page.clickOnTwitter()

