from selenium.webdriver.common.by import By
import random

class FormAboutRentLocatars:
    #Заголовок формы
    form_title = (By.XPATH, "//div[contains(text(),'Про аренду')]")
    #Поле для ввода "Когда привести самокат"
    field_when_to_bring = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    #Выбор даты
    date = (By.XPATH, "//div[contains(@class, '-selected')]")
    #Поле для ввода "срок аренды"
    rental_period_field = (By.XPATH, "//div[contains(text(),'Срок аренды')]/..")
    #Комментарий
    comment = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    #Кнопка для окончания заказа "Заказ"
    button_to_end = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[contains(text(),'Заказать')]")

    #Выбор цвета
    def color_scootars(self, color):
        if color == 1:
            #Поле для ввода "черный жемчуг"
            return (By.XPATH, "//input[@id='black']/..")
        else:
            #Поле для ввода "серая безысходность"
            return (By.XPATH, "//input[@id='grey']/..")

    #Меню для ввода "срок аренды"
    menu_rental_period = (By.XPATH, "//div[contains(text(),'сутки')]/../div["+str(random.randint(1,7))+"]")