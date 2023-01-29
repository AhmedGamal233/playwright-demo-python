import pytest
import allure
from allure_commons._allure import step
from pages.Result import ResultPage
from pages.search import SearchPage
from utils.Utilites import *
from playwright.sync_api import sync_playwright,expect, Page

@allure.title('Search tests')
@allure.story('Search')
class TestSearch:
    @staticmethod
    @pytest.mark.US
    @allure.title('Search Results')
    @pytest.mark.parametrize("searches,rest_of_search",read_test_data_from_csv_multi_col())
    def test_basic(
        searches,
        rest_of_search,
        base_url,
        page: Page,
        search_page: SearchPage,
        result_page: ResultPage):
        
        with step('# Given the DuckDuckGo home page is displayed'):
            search_page.load(base_url)
        with step('# When the user searches for a phrase'):
            search_page.search(f'{searches}')
        with step('# Then the search result query is the phrase'):
            page.wait_for_load_state()
            expect(result_page.search_input).to_have_value(f'{searches}')
        with step('# And the search result links pertain to the phrase'):
            assert result_page.result_link_titles_contain_phrase(f'{searches}')
        with step("# And the search result title contains the phrase"):
            expect(page).to_have_title(f'{searches}{rest_of_search}')
        with step("scroll to Twitter and tap on it"):
            result_page.scrollToTwitter()
            result_page.clickOnTwitter()

