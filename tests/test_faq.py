import allure
import pytest

from data import FAQ_DATA


@allure.feature("Главная страница")
@allure.story("Выпадающий список «Вопросы о важном»")
class TestFaq:
    @allure.title("При клике на вопрос «{question}» открывается правильный ответ")
    @pytest.mark.parametrize(
        "index, question, answer",
        FAQ_DATA,
        ids=[f"question_{item[0]}" for item in FAQ_DATA],
    )
    def test_faq_answer_opens_on_click(self, main_page, index, question, answer):
        main_page.click_faq_question(index)
        assert main_page.get_faq_answer_text(index) == answer
