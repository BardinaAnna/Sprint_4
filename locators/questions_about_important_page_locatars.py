from selenium import webdriver
from selenium.webdriver.common.by import By

class QuestionsAboutImportantLocatars:
    #заголовок страницы
    page_title = (By.XPATH, "//div[contains(text(),'Вопросы о важном')]")
    #аркадион
    arcadion = (By.XPATH, "//div[@class='arccadion']")
    #первый вопрос
    question_1 = (By.ID, "accordion__heading-0")
    #ответ на первый вопрос
    answer_1 = (By.XPATH, "//div[@id='accordion__panel-0']/p")
    #второй вопрос
    question_2 = (By.ID, "accordion__heading-1")
    #ответ на второй вопрос
    answer_2 = (By.XPATH, "//div[@id='accordion__panel-1']/p")
    #третий вопрос
    question_3 = (By.ID, "accordion__heading-2")
    #ответ на третий вопрос
    answer_3 = (By.XPATH, "//div[@id='accordion__panel-2']/p")
    #четвертый вопрос
    question_4 = (By.ID, "accordion__heading-3")
    #ответ на четвертый вопрос
    answer_4 = (By.XPATH, "//div[@id='accordion__panel-3']/p")
    #пятый вопрос
    question_5 = (By.ID, "accordion__heading-4")
    #ответ на пятый вопрос
    answer_5 = (By.XPATH, "//div[@id='accordion__panel-4']/p")
    #шестой вопрос
    question_6 = (By.ID, "accordion__heading-5")
    #ответ на шестой вопрос
    answer_6 = (By.XPATH, "//div[@id='accordion__panel-5']/p")
    #седьмой вопрос
    question_7 = (By.ID, "accordion__heading-6")
    #ответ на седьмой вопрос
    answer_7 = (By.XPATH, "//div[@id='accordion__panel-6']/p")
    #восьмой вопрос
    question_8 = (By.ID, "accordion__heading-7")
    #ответ на восьмой вопрос
    answer_8 = (By.XPATH, "//div[@id='accordion__panel-7']/p")


