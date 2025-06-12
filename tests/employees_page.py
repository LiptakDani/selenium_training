from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class EmployeesPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def go(self):
        self.driver.get("http://127.0.0.1:5025/")
        self.input_field = self.driver.find_element(By.ID, "name")
        self.save_button = self.driver.find_element(By.ID, "submit-input")
        self.employees_table = self.driver.find_elements(By.CSS_SELECTOR, "table")

    def fill_input(self, name: str) -> None:
        self.input_field.clear()
        self.input_field.send_keys(name)

    def click_save_button(self) -> None:
        self.save_button.click()

    def get_employees(self) -> list[str]:
        return [emp.text for emp in self.employees_list]
