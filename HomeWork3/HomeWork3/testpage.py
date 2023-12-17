from HomeWork3.HomeWork3.BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


# класс поиска локаторов
class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.XPATH, """//*[@id="login"]/div[3]/button""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_RESULT_LOGIN = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")

    LOCATOR_CREATE_NEW_POST = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_POST_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_POST_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_CREATE_POST_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_POST = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")

    LOCATOR_BTN_CONTACT = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_RESULT_SWITCHIHG_TO_FORM = (By.XPATH, """//*[@id="app"]/main/div/div/h1""")
    LOCATOR_FIELD_YOUR_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_FIELD_YOUR_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_FIELD_CONTENT_TO_FORM = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_BTN_CONTACT_US = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


# класс с методами (действиями с локаторами из файла test_1)

class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info(f"Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_text_blog(self):
        text_field = self.find_element(TestSearchLocators.LOCATOR_RESULT_LOGIN, time=2)
        text = text_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_RESULT_LOGIN[1]}")
        return text

    def click_nwe_post_button(self):
        logging.info(f"Click new post button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_NEW_POST).click()

    def enter_title_post(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_POST_TITLE[1]}")
        title_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE)
        title_field.clear()
        title_field.send_keys(word)

    def enter_content_post(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_POST_CONTENT[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_POST_CONTENT)
        content_field.clear()
        content_field.send_keys(word)

    def click_create_nwe_post_button(self):
        logging.info(f"Click new post button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()

    def post(self):
        post_field = self.find_element(TestSearchLocators.LOCATOR_POST, time=2)
        text = post_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_POST[1]}")
        return text

    def click_сontact_button(self):
        logging.info(f"Click сontact button")
        self.find_element(TestSearchLocators.LOCATOR_BTN_CONTACT).click()

    def result_switcying_to_form_text(self):
        result_field = self.find_element(TestSearchLocators.LOCATOR_RESULT_SWITCHIHG_TO_FORM, time=2)
        text = result_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_RESULT_SWITCHIHG_TO_FORM[1]}")
        return text

    def enter_name(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_FIELD_YOUR_NAME[1]}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_FIELD_YOUR_NAME)
        name_field.clear()
        name_field.send_keys(word)

    def enter_email(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_FIELD_YOUR_EMAIL[1]}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_FIELD_YOUR_EMAIL)
        name_field.clear()
        name_field.send_keys(word)

    def enter_content_to_form(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_FIELD_CONTENT_TO_FORM[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_FIELD_CONTENT_TO_FORM)
        content_field.clear()
        content_field.send_keys(word)

    def click_contact_us_button(self):
        logging.info(f"Click login button")
        self.find_element(TestSearchLocators.LOCATOR_BTN_CONTACT_US).click()

    def get_alert_text(self):
        alert_field = self.driver.switch_to.alert
        text = alert_field.text
        logging.info(f"We find text {text} in alert")
        return text
