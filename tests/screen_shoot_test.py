from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def test_grid(driver: WebDriver):
    driver.get("http://127.0.0.1:5500/pages/grid/")
    driver.save_screenshot("grid_test.png")
    element = driver.find_element(By.CSS_SELECTOR, "body > table > tbody > tr:nth-child(2) > td:nth-child(2)")
    element.screenshot("grid_element.png")