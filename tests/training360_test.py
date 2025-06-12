import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def test_link(driver: WebDriver):
    # Given
    driver.get(
        "https://www.training360.com/tesztautomatizalas-selenium-webdriverrel-pythonban-tanfolyam-swd-python"
    )
    link = driver.find_element(By.PARTIAL_LINK_TEXT, "itt olvashat")
    assert "/egyedi-oktatasi" in link.get_attribute("href")


def test_price_by_class_name(driver: WebDriver):
    # Given
    driver.get(
        "https://www.training360.com/tesztautomatizalas-selenium-webdriverrel-pythonban-tanfolyam-swd-python"
    )
    price = driver.find_element(By.CLASS_NAME, "selected-course__amount")
    assert price.text == "377 520 Ft", (
        f"The price should be '377 520 Ft' but got {price.text}"
    )


def test_price_by_css_selector(driver: WebDriver):
    # Given
    driver.get(
        "https://www.training360.com/tesztautomatizalas-selenium-webdriverrel-pythonban-tanfolyam-swd-python"
    )
    price = driver.find_element(By.CSS_SELECTOR, ".selected-course__amount")
    assert price.text == "377 520 Ft", (
        f"The price should be '377 520 Ft' but got {price.text}"
    )


def test_tematika_by_css_selector(driver: WebDriver):
    # Given
    driver.get(
        "https://www.training360.com/tesztautomatizalas-selenium-webdriverrel-pythonban-tanfolyam-swd-python"
    )
    tematika_elements = [
        element.text for element in driver.find_elements(By.CSS_SELECTOR, "#Outline li")
    ]
    print(tematika_elements)
    assert tematika_elements[0] == "Webes alkalmazások felépítése"


def test_tematika_by_xpath(driver: WebDriver):
    # Given
    driver.get(
        "https://www.training360.com/tesztautomatizalas-selenium-webdriverrel-pythonban-tanfolyam-swd-python"
    )
    tematika_elements = [
        element.text
        for element in driver.find_elements(By.XPATH, '//*[@id="C_Outline"]/ul/li')
    ]
    print(tematika_elements)
    assert tematika_elements[0] == "Webes alkalmazások felépítése"


def test_outline_performance(driver: WebDriver):
    # Given
    driver.get(
        "https://www.training360.com/tesztautomatizalas-selenium-webdriverrel-pythonban-tanfolyam-swd-python"
    )
    c_outline_dive = driver.find_element(By.CSS_SELECTOR, "#C_Outline")
    title_elements = c_outline_dive.find_elements(By.CSS_SELECTOR, "p > b")
    titles = [element.text for element in title_elements]
    print(titles)
    list_elements = c_outline_dive.find_elements(By.CSS_SELECTOR, "ul > li")
    list_items = [element.text for element in list_elements]
    print(list_items)
    assert titles[0] == "Technológiai bevezetés"
    assert list_items[0] == "Webes alkalmazások felépítése"
