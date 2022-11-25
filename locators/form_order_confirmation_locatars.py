from selenium.webdriver.common.by import By

class FormOrderConfirmationLocatars:
    #Заголовок формы
    form_title = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
    #Кнопка подтверждения заказа
    button_yes = (By.XPATH, "//button[contains(text(),'Да')]")