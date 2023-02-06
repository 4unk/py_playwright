import pytest
import pages


class TestFooter:
    def test_lucky_button_text(self, page):
        pages.index_page.open_index_page(page)
        actual_res_lb = pages.lucky_button.get_text_from_lucky_button(page)
        assert actual_res_lb == "Мне повезёт!", "Google lucky button text is not correct"