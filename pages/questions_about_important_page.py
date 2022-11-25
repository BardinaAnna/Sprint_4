import allure

from locators.questions_about_important_page_locatars import QuestionsAboutImportantLocatars as QAIL
from pages.base_page import BasePage



class QuestionsAboutImportantPage(BasePage):

    @allure.step("Ищем заголовок страницы 'Важные вопросы'")
    def find_title(self):
        return self.find_element(QAIL.page_title)

    @allure.step("Открываем первый ответ")
    def click_1_question(self):
        self.scroll_element(QAIL.question_1)
        return self.click_element(QAIL.question_1)

    @allure.step("Находим текст первого ответа")
    def find_1_answer(self):
        return self.find_element(QAIL.answer_1)

    @allure.step("Открываем второй ответ")
    def click_2_question(self):
        self.scroll_element(QAIL.question_2)
        return self.click_element(QAIL.question_2)

    @allure.step("Находим текст второго ответа")
    def find_2_answer(self):
        return self.find_element(QAIL.answer_2)

    @allure.step("Открываем третий ответ")
    def click_3_question(self):
        self.scroll_element(QAIL.question_3)
        return self.click_element(QAIL.question_3)

    @allure.step("Находим текст третьего ответа")
    def find_3_answer(self):
        return self.find_element(QAIL.answer_3)

    @allure.step("Открываем четвертый ответ")
    def click_4_question(self):
        self.scroll_element(QAIL.question_4)
        return self.click_element(QAIL.question_4)

    @allure.step("Находим текст четвертого ответа")
    def find_4_answer(self):
        return self.find_element(QAIL.answer_4)

    @allure.step("Открываем пятый ответ")
    def click_5_question(self):
        self.scroll_element(QAIL.question_5)
        return self.click_element(QAIL.question_5)

    @allure.step("Находим текст пятого ответа")
    def find_5_answer(self):
        return self.find_element(QAIL.answer_5)

    @allure.step("открываем шестой ответ")
    def click_6_question(self):
        self.scroll_element(QAIL.question_6)
        return self.click_element(QAIL.question_6)

    @allure.step("Находим текст шестого ответа ")
    def find_6_answer(self):
        return self.find_element(QAIL.answer_6)

    @allure.step("Открываем седьмой ответ")
    def click_7_question(self):
        self.scroll_element(QAIL.question_7)
        return self.click_element(QAIL.question_7)

    @allure.step("Находим текст седьмого ответа")
    def find_7_answer(self):
        return self.find_element(QAIL.answer_7)

    @allure.step("Открываем восьмой ответ")
    def click_8_question(self):
        self.scroll_element(QAIL.question_8)
        return self.click_element(QAIL.question_8)

    @allure.step("Находим текст восьмого овтета")
    def find_8_answer(self):
        return self.find_element(QAIL.answer_8)