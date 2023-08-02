from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException


class Test_Credence_003:

    def test_Credkart_Login_006(self):
        driver = webdriver.Firefox()
        driver.get("https://automation.credence.in/login")
        driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys("snehacredence@test.com")
        driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("test$1234")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Login Test Case is Passed")
            assert True
        except NoSuchElementException:
            print("Login Test Case is Failed")
            assert False
