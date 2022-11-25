import allure

from pages.questions_about_important_page import QuestionsAboutImportantPage as QAIP

class TestQuestionsAboutImportant:
    @allure.suite("Проверка страницы 'Вопросы о важном'")
    @allure.feature("Что страница присутствует")
    @allure.story("Промотав вниз страницы мы переходим на старницу 'Вопросы о важном'")
    def test_presence_of_title_questions_about_important_title_is_present(self, driver):
        title_questions = QAIP(driver)
        assert title_questions.find_title().text == 'Вопросы о важном'

    @allure.suite("Проверка страницы 'Вопросы о важном'")
    @allure.feature("Проверяем текст первого ответа")
    @allure.story("Раскрываем первый вопрос и проверяем текст")
    def test_click_1_question_response_text_corresponds_to(self, driver):
        question1 = QAIP(driver)
        question1.click_1_question()
        assert question1.find_1_answer().text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.suite("Проверка страницы 'Вопросы о важном'")
    @allure.feature("Проверяем текст второго ответа")
    @allure.story("Раскрываем второй вопрос и проверяем текст")
    def test_click_2_question_response_text_corresponds_to(self, driver):
        question2 = QAIP(driver)
        question2.click_2_question()
        assert question2.find_2_answer().text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.suite("Проверка страницы 'Вопросы о важном'")
    @allure.feature("Проверяем текст третьего ответа")
    @allure.story("Раскрываем третий вопрос и проверяем текст")
    def test_click_3_question_response_text_corresponds_to(self, driver):
        question3 = QAIP(driver)
        question3.click_3_question()
        assert question3.find_3_answer().text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.suite("Проверка страницы 'Вопросы о важном'")
    @allure.feature("Проверяем текст четвертый ответа")
    @allure.story("Раскрываем четвертого вопрос и проверяем текст")
    def test_click_4_question_response_text_corresponds_to(self, driver):
        question4 = QAIP(driver)
        question4.click_4_question()
        assert question4.find_4_answer().text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.suite("Проверка страницы 'Вопросы о важном'")
    @allure.feature("Проверяем текст пятого ответа")
    @allure.story("Раскрываем пятый вопрос и проверяем текст")
    def test_click_5_question_response_text_corresponds_to(self, driver):
        question5 = QAIP(driver)
        question5.click_5_question()
        assert question5.find_5_answer().text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.suite("Проверка страницы 'Вопросы о важном'")
    @allure.feature("Проверяем текст шестого ответа")
    @allure.story("Раскрываем шестой вопрос и проверяем текст")
    def test_click_6_question_response_text_corresponds_to(self, driver):
        question6 = QAIP(driver)
        question6.click_6_question()
        assert question6.find_6_answer().text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.suite("Проверка страницы 'Вопросы о важном'")
    @allure.feature("Проверяем текст седьмого ответа")
    @allure.story("Раскрываем седьмой вопрос и проверяем текст")
    def test_click_7_question_response_text_corresponds_to(self, driver):
        question7 = QAIP(driver)
        question7.click_7_question()
        assert question7.find_7_answer().text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.suite("Проверка страницы 'Вопросы о важном'")
    @allure.feature("Проверяем текст восьмого ответа")
    @allure.story("Раскрываем восьмой вопрос и проверяем текст")
    def test_click_8_question_response_text_corresponds_to(self, driver):
        question8 = QAIP(driver)
        question8.click_8_question()
        assert question8.find_8_answer().text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'