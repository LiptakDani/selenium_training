import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_say_hello():
    # Given
    NAME = "Lipták Dániel"

    # When
    messages = f"Hello, {NAME}!"

    # Then
    assert messages == "Hello, Lipták Dániel!", (
        "The message should be 'Hello, Lipták Dániel!'"
    )


def test_selenium_say_hello():
    # Given
    NAME = "Lipták Dániel"

    options = Options()
    # options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://127.0.0.1:5500/pages/welcome/")
    driver.maximize_window()

    # when
    input_field = driver.find_element(By.ID, "name-input")
    input_field.send_keys(NAME)

    button = driver.find_element(By.ID, "welcome-button")
    button.click()

    # Then
    message_div = driver.find_element(By.ID, "welcome-div").text
    assert message_div == f"Hello {NAME}!", "The message should be different"


