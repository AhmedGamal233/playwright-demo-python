from playwright.sync_api import Page,TimeoutError
from configparser import ConfigParser

class SearchPage:
    URL = 'https://www.duckduckgo.com'
    search_button ="#search_button_homepage" 
    search_input ="#search_form_input_homepage"
    search_button_chrome ="Search" 
    search_input_chrome ="#searchbox_input" 
    def __init__(self, page: Page):
        self.page = page
        self.search_input_locator_chrome = page.locator(SearchPage.search_input_chrome)
        self.search_input_locator = page.locator(SearchPage.search_input)
        self.search_button_locator_chrome  = page.get_by_role("button",name=SearchPage.search_button_chrome).nth(1)
        self.search_button_locator  = page.locator(SearchPage.search_button)
            
        
    def load(self,base_url) -> None:
        self.page.goto(base_url)
        
    def search(self, phrase: str) -> None:
        try:
            self.search_input_locator.fill(phrase,timeout=1000) 
            self.search_button_locator.click(timeout=1000)
        except TimeoutError:
            self.search_input_locator_chrome.fill(phrase) 
            self.search_button_locator_chrome.click()
