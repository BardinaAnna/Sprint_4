import allure

from locators.form_about_rent_locatars import FormAboutRentLocatars as FARL
from pages.base_page import BasePage



class FormAboutRentPage(BasePage):

    @allure.step("Ищем заголовок страницы 'Про аренду'")
    def find_title_about_rent(self):
        return self.find_element(FARL.form_title)

    @allure.step("Вводим данные в поле 'Когда привезти самокат'")
    def input_date(self):
        self.click_element(FARL.field_when_to_bring)
        return self.click_element(FARL.date)

    @allure.step("Вводим данные в поле 'Срок аренды'")
    def input_rental_period(self):
        self.click_element(FARL.rental_period_field)
        return self.click_element(FARL.menu_rental_period)

    @allure.step("Выбираем цвет самоката")
    def input_color_scooter(self, color):
        color_class = FARL()
        return self.click_element(color_class.color_scootars(color))

    @allure.step("Вводим данные в поле 'Комментарий'")
    def input_comment(self):
        return self.input_element(FARL.comment, "Новенький бы")

    @allure.step("Нажимаем на кнопку 'Заказать'")
    def click_order_button(self):
        return self.click_element(FARL.button_to_end)
