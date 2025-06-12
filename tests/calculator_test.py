import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def read_file():
    with open("tests\calculator.csv") as file:
        lines = file.readlines()
        data = []
        for line in lines:
            a, b, expected = line.strip().split(",")
            data.append((int(a), int(b), int(expected)))
        return data


@pytest.mark.parametrize("a, b, expected", read_file())
def test_calculator_add_2_number(driver: WebDriver, a: int, b: int, expected: int):
    print("test")
    a_input = driver.find_element(By.ID, "a-input")
    a_input.send_keys(a)

    b_input = driver.find_element(By.ID, "b-input")
    b_input.send_keys(b)

    submit_button = driver.find_element(By.ID, "submit-button")
    submit_button.click()

    result_input = driver.find_element(By.ID, "result-input").get_attribute("value")
    assert result_input == str(expected), (
        "The result should be {expected} but got {result_input}"
    )
