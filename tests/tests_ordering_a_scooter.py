import allure

from pages.form_for_whom_is_scooter_page import FormForWhomScooterPage as FFWSP
from pages.form_about_rent_page import FormAboutRentPage as FARP
from pages.home_page import HomePage as HP
from pages.form_order_confirmation_page import FormOrderConfirmationPage as FOCP
from pages.form_order_has_been_placed_page import FormOrderHasBeenPlacedPage as FOHBPP

class TestOrderingScooter:
    @allure.suite("Тест на проверку перехода на страницу 'Для кого самокат' при нажатии на кнопку 'Заказать'")
    @allure.feature("Тест по верхней кнопки заказать")
    @allure.story("При нажатии на кнопку 'Заказать', происходит переход на форму заказа")
    def test_top_order_button_form_for_whom_scooter_opens(self, driver):
        driver_HP = HP(driver)
        driver_HP.click_top_order_button()
        driver_FFWSP = FFWSP(driver)
        assert driver_FFWSP.find_title_who_is_scooter_for().text == 'Для кого самокат'

    @allure.suite("Тест на проверку перехода на страницу 'Для кого самокат' при нажатии на кнопку 'Заказать'")
    @allure.feature("Тест по нижней кнопки заказать")
    @allure.story("При нажатии на кнопку 'Заказать', происходит переход на форму заказа")
    def test_on_order_button_form_for_whom_scooter_opens(self, driver):
        driver_HP = HP(driver)
        driver_HP.click_on_order_button()
        driver_FFWSP = FFWSP(driver)
        assert driver_FFWSP.find_title_who_is_scooter_for().text == 'Для кого самокат'

    @allure.suite("Позитивный тест оформление заказа")
    @allure.feature("Заполнение полей формы 'Для кого самокат'")
    @allure.story("После нажатия на кнопку 'Далее' происходит переход на форму 'Про аренду'")
    def test_filling_out_form_for_whom_scooter_form_about_renting_opens(self, driver):
        driver_HP = HP(driver)
        driver_HP.click_top_order_button()
        driver_FFWSP = FFWSP(driver)
        driver_FFWSP.input_name_field('Анна')
        driver_FFWSP.input_last_name_field('Муровна')
        driver_FFWSP.input_address_field('Беларусская 8 190')
        driver_FFWSP.input_metro()
        driver_FFWSP.input_phone('89269999999')
        driver_FFWSP.click_next()
        driver_FARP = FARP(driver)
        assert driver_FARP.find_title_about_rent().text == 'Про аренду'

    @allure.suite("Позитивный тест оформление заказа")
    @allure.feature("Заполнение полей формы 'Про аренду'")
    @allure.story("После нажатия на кнопку 'Заказать' происходит переход в модальное окно подтверждение заказа")
    def test_filling_out_rental_form_the_open_order_confirmation_window_will(self, who_is_scooter):
        driver_FARP = FARP(who_is_scooter)
        driver_FARP.input_date()
        driver_FARP.input_rental_period()
        driver_FARP.input_color_scooter(2)
        driver_FARP.input_comment()
        driver_FARP.click_order_button()
        driver_FOCP = FOCP(who_is_scooter)
        assert driver_FOCP.find_title().text == "Хотите оформить заказ?\n "

    @allure.suite("Позитивный тест оформление заказа")
    @allure.feature("Подтверждение заказа")
    @allure.story("После нажатия на кнопку 'Да' для подтверждения заказа открывается форма подтверждения заказа")
    def test_order_confirmation_order_will_be_confirmed(self, about_rent):
        driver_FOCP = FOCP(about_rent)
        driver_FOCP.click_button_yas()
        driver_FOHBPP = FOHBPP(about_rent)
        assert driver_FOHBPP.find_button_status().text == "Посмотреть статус"




