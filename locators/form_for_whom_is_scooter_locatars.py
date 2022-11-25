from selenium.webdriver.common.by import By

class FormForWhomScooterLocatars:
    #Заголовок формы
    form_title = (By.XPATH, "//div[contains(text(),'Для кого самокат')]")
    #Поле для ввода "Имя"
    name_field = (By.XPATH, "//input[@placeholder='* Имя']")
    # Поле для ввода "Фамилия"
    last_name_field = (By.XPATH, "//input[@placeholder='* Фамилия']")
    # Поле для ввода "Адрес"
    address_field = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    # Поле для ввода "Станция метро"
    metro_address_field = (By.XPATH, "//input[@placeholder='* Станция метро']")

    #Список метро
    list_metro = (By.XPATH, "//div[@class='select-search has-focus']/div[2]")

    # Поле для ввода "Телефон"
    phone_field = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    # Кнопка "Далее"
    next_button = (By.XPATH, "//button[contains(text(),'Далее')]")

