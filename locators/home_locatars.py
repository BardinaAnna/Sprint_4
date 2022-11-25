from selenium.webdriver.common.by import By

class HomeLocatars:
    #Вверхняя кнопка "Заказать"
    top_order_button = (By.XPATH, "//button[contains(text(),'Заказать') and @class='Button_Button__ra12g']")
    #Нижняя кнопка "Заказать"
    on_order_button = (By.XPATH, "//div[@class ='Home_FinishButton__1_cWm']/button[contains(text(), 'Заказать')]")
    #Логотип самокат
    scooter_logo = (By.XPATH, "//img[@alt='Scooter']")
    #Логотип Яндекс
    yandex_logo = (By.XPATH, "//img[@alt='Yandex']")
    #Кнопка "статус заказа"
    order_status = (By.XPATH, "//button[contains(text(),'Статус заказа')]")
    #Поле для ввода номера заказа
    order_number_input_field = (By.XPATH, "//input[@placeholder='Введите номер заказа']")
    #Кнопка "Go!"
    button_GO = (By.XPATH, "//button[contains(text(),'Go!')]")