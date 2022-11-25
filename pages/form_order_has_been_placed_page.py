import allure
from pages.base_page import BasePage
from locators.form_order_has_been_placed_locatars import FormOrderHasBeenPlacedLocatars as FOHBPL

class FormOrderHasBeenPlacedPage(BasePage):

    @allure.step("Ищем кнопку 'Посмотреть статус' для подтверждения, что окно подтверждающее заказ открылось")
    def find_button_status(self):
        return self.find_element(FOHBPL.button_status)