from playwright.sync_api import Page
import config


class LuckyButton:
    _BUTTON_IM_FEELING_LUCKY = "//div[@class='FPdoLc lJ9FBc']//input[@name='btnI']"
        
    def get_text_from_lucky_button(self, page: Page) -> None:
        return page.locator(self._BUTTON_IM_FEELING_LUCKY).get_attribute('value')