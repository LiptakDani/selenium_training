from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


def test_navigation(driver: WebDriver):
    driver.get("http://127.0.0.1:5500/pages/wizard/")
    driver.find_element(By.LINK_TEXT, "Next").click()
    driver.find_element(By.LINK_TEXT, "Next").click()
    driver.back()
    header = driver.find_element(By.TAG_NAME, "h1")
    assert header.text == "Wizard1", "Expected to be on Step 2" 