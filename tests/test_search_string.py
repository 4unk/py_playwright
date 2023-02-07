#from playwright.sync_api import Playwright, sync_playwright, expect
import pages
import pytest

#def run(playwright: Playwright) -> None:
#    browser = playwright.chromium.launch(headless=False)
#    context = browser.new_context()
#    page = context.new_page()
class TestFooter:    
    def open_search_results(self, page):    
    #page.goto("https://www.google.com/?gws_rd=ssl")
        pages.index_page.open_index_page(page)
        page.get_by_role("combobox", name="Найти").click()
        page.get_by_role("combobox", name="Найти").fill("playwright")
        page.get_by_role("combobox", name="Найти").press("Enter")
        page.get_by_role("link", name="Playwright: Fast and reliable end-to-end testing for modern ... https://playwright.dev").click()
        page.get_by_role("link", name="Get started").click()
    
    # ---------------------
        context.close()
        browser.close()


#with sync_playwright() as playwright:
 #   run(playwright)
