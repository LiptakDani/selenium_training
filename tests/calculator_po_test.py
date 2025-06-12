from selenium.webdriver.remote.webdriver import WebDriver as Webdriver
from tests.calculator_po import CalculatorPage


def test_calculate(driver: Webdriver):
    calculator = CalculatorPage(driver)
    calculator.go()
    calculator.fill_inputs(2, 3)
    result = calculator.click_add_button()
    result = calculator.get_result()
    assert result == 5