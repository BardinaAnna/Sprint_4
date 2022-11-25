import allure
from locators.form_order_status_locatars import FormOrderStatusLocatars as FOSL
from pages.base_page import BasePage

class FormOrderStatusPage(BasePage):

    @allure.step("Нажимаем кнопку 'Посмотреть'")
    def find_button_watch(self):
        return self.find_element(FOSL.button_watch)