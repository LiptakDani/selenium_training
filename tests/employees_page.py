from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class EmployeesPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def go(self):
        self.driver.get("http://127.0.0.1:5025/")


    def set_name(self, name: str = "Jhon Doe") -> None:
        name_input = self.driver.find_element(By.ID, "name")
        name_input.clear()
        name_input.send_keys(name)

    def click_save_button(self) -> None:
        save_button = self.driver.find_element(By.ID, "submit-input")
        save_button.click()

    def get_table_dictionary(self) -> list:
        tr_elements = self.driver.find_elements(By.CSS_SELECTOR, "tbody > tr")
        rows = []
        for tr in tr_elements:
            td_elements = tr.find_elements(By.CSS_SELECTOR, "td")
            rows.append((td_elements[0].text, td_elements[1].text))
        return rows

    def wait_for_message(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "message-paragraph")))