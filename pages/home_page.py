import allure

from locators.home_locatars import HomeLocatars as HL
from pages.base_page import BasePage

class HomePage(BasePage):

    @allure.step("Нажимаем вверхнюю кнопку 'Заказать'")
    def click_top_order_button(self):
        return self.click_element(HL.top_order_button)

    @allure.step("Нажимаем нижнюю кнопку 'Заказать'")
    def click_on_order_button(self):
        self.scroll_element(HL.on_order_button)
        return self.click_element(HL.on_order_button)

    @allure.step("Нажимаем на слово 'Самокат' в логотипе")
    def click_scooter_logo(self):
        return self.click_element(HL.scooter_logo)

    @allure.step("Нажимаем на кнопку 'Статус заказа'")
    def click_order_status(self):
        return self.click_element(HL.order_status)

    @allure.step("Ищем поле 'Введите номер заказа'")
    def find_number_order(self):
        return self.find_element(HL.order_number_input_field)

    @allure.step("Нажимаем кнопку 'Go!'")
    def click_button_go(self):
        return self.click_element(HL.button_GO)

    #@allure.step("нажимаем на слово 'Яндекс' в логотипе")
    def click_logo_yandex(self):
        self.click_element(HL.yandex_logo)