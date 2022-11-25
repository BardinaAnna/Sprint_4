import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage as HP

class TestClickThroughToYandex:
    @allure.suite("Тест на проверку перехода на гланвую страницу Яндекса по клику на слово 'Яндекс' в логотипе")
    @allure.feature("Тест перехода с любого места")
    @allure.story("При нажатии на слово 'Яндекс' в логотипе, происходит переход на главную страницу Яндекса в новом окне браузера")
    def test_click_through_to_yandex_open_dzen_page(self, driver):
        driver.implicitly_wait(10)
        driver_HP = HP(driver)
        driver_HP.click_logo_yandex()
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 30).until(EC.url_to_be('https://dzen.ru/?yredirect=true'))
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'