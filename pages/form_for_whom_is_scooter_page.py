import allure

from locators.form_for_whom_is_scooter_locatars import FormForWhomScooterLocatars as FFWSL
from pages.base_page import BasePage


class FormForWhomScooterPage(BasePage):
    #@allure.step("Ищем заголовок страницы 'Для кого самокат'")
    def find_title_who_is_scooter_for(self):
        return self.find_element(FFWSL.form_title)

    #@allure.step("Вводим данные в поле 'Имя'")
    def input_name_field(self, name):
        return self.input_element(FFWSL.name_field, name)

    #@allure.step("Вводим данные в поле 'Фамилия'")
    def input_last_name_field(self, last_name):
        return self.input_element(FFWSL.last_name_field, last_name)

    #@allure.step("Вводим данные в поле 'Адрес'")
    def input_address_field(self, address):
        return self.input_element(FFWSL.address_field, address)

    #@allure.step("Выбираем станцию метро")
    def input_metro(self):
        self.click_element(FFWSL.metro_address_field)
        return self.click_element(FFWSL.list_metro)

    #@allure.step("Вводим данные в поле 'Телефон'")
    def input_phone(self, phone):
        return self.input_element(FFWSL.phone_field, phone)

    #@allure.step("Нажимаем на кнопку 'Далее'")
    def click_next(self):
        return self.click_element(FFWSL.next_button)