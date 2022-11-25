import allure
from selenium import webdriver
import pytest
from pages.form_for_whom_is_scooter_page import FormForWhomScooterPage as FFWSP
from pages.home_page import HomePage as HP
from pages.form_about_rent_page import FormAboutRentPage as FARP


@pytest.fixture(scope='function')
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--headless')
    driver = webdriver.Firefox('C:\\WebDriver\\bin', options=firefox_options)
    driver.get('https://qa-scooter.praktikum-services.ru/')

    yield driver

    driver.quit()

@pytest.fixture()
def who_is_scooter(driver):
    driver_HP = HP(driver)
    driver_HP.click_top_order_button()
    driver_FFWSP = FFWSP(driver)
    driver_FFWSP.input_name_field('Анна')
    driver_FFWSP.input_last_name_field('Муровна')
    driver_FFWSP.input_address_field('Беларусская 8 190')
    driver_FFWSP.input_metro()
    driver_FFWSP.input_phone('89269999999')
    driver_FFWSP.click_next()
    return driver

@pytest.fixture()
def about_rent(who_is_scooter):
    driver_FARP = FARP(who_is_scooter)
    driver_FARP.input_date()
    driver_FARP.input_rental_period()
    driver_FARP.input_color_scooter(2)
    driver_FARP.input_comment()
    driver_FARP.click_order_button()
    return who_is_scooter