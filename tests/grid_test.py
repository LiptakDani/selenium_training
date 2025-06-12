import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.relative_locator import locate_with


def test_grid(driver: WebDriver):
    driver.get("http://127.0.0.1:5500/pages/grid/")
    element5 = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) td:nth-child(2)")
    assert element5.text == "5", f"Expected '5' but got '{element5.text}'"

    # relative
    element4 = driver.find_element(
        locate_with(By.CSS_SELECTOR, "td").to_left_of(element5)
    )
    assert element4.text == "4", f"Expected '2' but got '{element4.text}'"
