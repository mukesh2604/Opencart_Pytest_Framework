from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    lnk_myaccount_xpath = "//a[@title='My Account']"
    lnk_register_linktext = "Register"
    lnk_login_linktext = "Login"

    def __init__(self, driver):
        self.driver = driver

    # element = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.ID, "element_id"))
    # )
    # element.click()
    def clickMyAccount(self,driver):
        # self.driver.find_element(By.XPATH, self.lnk_myaccount_xpath).click()
        self.element = WebDriverWait(self.driver, 100).until(

            EC.element_to_be_clickable((By.ID, "element_id"))
        )
        self.element.click()

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_register_linktext).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_login_linktext).click()
