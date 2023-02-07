from playwright.sync_api import Page
import config


class SearchString:
    _SEARCH_STRING = "//div[@class='YacQv']"
    
    def find_search_string(self, page: Page) -> None:
        page.locator(self._SEARCH_STRING).click()