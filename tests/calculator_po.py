from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def go(self):
        self.driver.get("http://127.0.0.1:5500/pages/calculator/")
        self.number1_input = self.driver.find_element(By.ID, "a-input")
        self.number2_input = self.driver.find_element(By.ID, "b-input")
        self.add_button = self.driver.find_element(By.ID, "submit-button")
        self.result = self.driver.find_element(By.ID, "result-input")

    def fill_inputs(self, num1: int, num2: int) -> None:
        self.number1_input.clear()
        self.number1_input.send_keys(num1)
        self.number2_input.clear()
        self.number2_input.send_keys(num2)

    def click_add_button(self) -> None:
        self.add_button.click()

    def get_result(self) -> int:
        return int(self.result.get_attribute("value"))

    def add(self, num1: int, num2: int) -> int:
        self.fill_inputs(num1, num2)
        self.click_add_button()
        return self.get_result()
