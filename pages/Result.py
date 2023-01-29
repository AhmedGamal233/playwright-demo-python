from playwright.sync_api import Page
# from typing import List

class ResultPage:
    twitter_icon="(//a[contains(@href,'twitter')])[last()]"
    result_links ="a[data-testid='result-title-a']"
    search_input="#search_form_input"
    def __init__(self, page: Page):
        self.page = page
        self.result_links = page.locator(ResultPage.result_links)
        self.search_input = page.locator(ResultPage.search_input)
    
    def result_link_titles(self):
        self.result_links.nth(4)
        return self.result_links.all_text_contents()
    
    def result_link_titles_contain_phrase(self, phrase: str, minimum: int = 1):
        titles = self.result_link_titles()
        matches = [t for t in titles if phrase.lower() in t.lower()]
        return len(matches) >= minimum
    
    def scrollToTwitter(self):
        while(not self.page.locator(ResultPage.twitter_icon).is_visible()):
            #mouse.wheel(x, y) x horizontall scroll ,y vertical
            # page.mouse.wheel(0, 5000)
            self.page.keyboard.down('PageDown') #also works
            if self.page.locator(self.twitter_icon).is_visible:
                break
    def clickOnTwitter(self):
        self.page.locator(self.twitter_icon).click()
