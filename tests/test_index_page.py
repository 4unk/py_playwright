import pytest
import pages
import time

class TestFooter:
    def test_user_should_be_able_to_open_popup(self, page):
        pages.index_page.open_index_page(page)
        time.sleep(5)