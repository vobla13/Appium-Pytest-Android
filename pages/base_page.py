from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




# BasePage locators:
privacy_link = (By.ID, "uk.co.aifactory.chessfree:id/Text_Privacy")
ok_btn = (By.ID, "uk.co.aifactory.chessfree:id/YesButton")


class BasePage:
    
    def __init__(self, driver):
        self._driver = driver

    

    def open_privacy_link(self):
        print('open_link')
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(((privacy_link)))
        ).click()

    
    def click_ok_btn(self):
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(((ok_btn)))
        ).click()