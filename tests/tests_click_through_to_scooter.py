import allure
from pages.home_page import HomePage as HP
from pages.form_for_whom_is_scooter_page import FormForWhomScooterPage as FFWSP
from pages.form_order_status_page import FormOrderStatusPage as FOSP

class TestClickThroughToScooter:
    @allure.suite("Тесты на проверку перехода на домашнюю страницу по клику на слово 'Самокат' в логотипе")
    @allure.feature("Тест перехода со страницы оформления заказа")
    @allure.story("При нажатии на слово 'Самокат' в логотипе, происходит переход на главную страницу")
    def test_click_through_to_scooter_order_form_go_home_page(self, driver):
        driver_HP = HP(driver)
        driver_HP.click_top_order_button()
        driver_FFWSP = FFWSP(driver)
        driver_FFWSP.find_title_who_is_scooter_for()
        driver_HP.click_scooter_logo()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.suite("Тесты на проверку перехода на домашнюю страницу по клику на слово 'Самокат' в логотипе")
    @allure.feature("Тест перехода со страницы статуса заказа")
    @allure.story("При нажатии на слово 'Самокат' в логотипе, происходит переход на главную страницу")
    def test_click_through_of_scooter_from_order_status_go_home_page(self, driver):
        driver_HP = HP(driver)
        driver_HP.click_order_status()
        driver_HP.click_button_go()
        driver_FOSP = FOSP(driver)
        driver_FOSP.find_button_watch()
        driver_HP.click_scooter_logo()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'