import allure
from pages.base_page import BasePage
from locators.form_order_confirmation_locatars import FormOrderConfirmationLocatars as FOCL

class FormOrderConfirmationPage(BasePage):

    @allure.step("Ищем заголовок модального окна подтверждения заказа")
    def find_title(self):
        return self.find_element(FOCL.form_title)

    @allure.step("Нажимаем кнопку 'Да'")
    def click_button_yas(self):
        return self.click_element(FOCL.button_yes)