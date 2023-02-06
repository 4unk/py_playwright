import pytest
import pages


class TestFooter:
    def test_user_should_be_able_to_open_popup(self, page):
        pages.index_page.open_index_page(page)
        actual_res_sb = pages.search_button.get_text_from_google_search_button(page)
        assert actual_res_sb == "Поиск в Google", "Google Search button text is not correct"
        
   
        
        