import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locatar):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locatar), message=f'Not find locator')

    def click_element(self, locator):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator), message=f'Not find locator').click()

    def input_element(self, locator, word):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator), message=f'Not find locator').send_keys(word)

    def scroll_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(locator))
