import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select


def test_finde_by_natural_if(driver: WebDriver):
    driver.get("http://127.0.0.1:5500/pages/components/")
    tr_elements = driver.find_elements(By.CSS_SELECTOR, "tbody > tr")
    for tr in tr_elements:
        td_elements = tr.find_elements(By.CSS_SELECTOR, "td")
        id = td_elements[0].text
        name = td_elements[1].text
        print(f"ID: {id}, Name: {name}")
        if id == "2":
            found_name = name
    assert found_name == "Jack Doe"


def test_table(driver: WebDriver):
    driver.get("http://127.0.0.1:5500/pages/components/")
    tr_elements = driver.find_elements(By.CSS_SELECTOR, "tbody > tr")
    rows = []
    for tr in tr_elements:
        td_elements = tr.find_elements(By.CSS_SELECTOR, "td")
        row = [td.text for td in td_elements]
        rows.append(row)
    print(rows)


def test_table_dictionary(driver: WebDriver):
    driver.get("http://127.0.0.1:5500/pages/components/")
    tr_elements = driver.find_elements(By.CSS_SELECTOR, "tbody > tr")
    rows = []
    headers = [th.text for th in driver.find_elements(By.CSS_SELECTOR, "thead th")]
    for tr in tr_elements:
        td_elements = tr.find_elements(By.CSS_SELECTOR, "td")
        row = {header: td.text for header, td in zip(headers, td_elements)}
        rows.append(row)
    print(rows)


def test_checkbox(driver: WebDriver):
    driver.get("http://127.0.0.1:5500/pages/components/")
    check_box = driver.find_element(By.NAME, "checkbox")
    assert not check_box.is_selected(), "Checkbox 1 should be selected after clicking"
    check_box.click()
    assert check_box.is_selected(), "Checkbox 1 should be selected after clicking"


def test_checkbox_disabled(driver: WebDriver):
    driver.get("http://127.0.0.1:5500/pages/components/")
    check_box = driver.find_element(By.NAME, "disabled-checkbox")
    assert not check_box.is_enabled()


def test_visibility(driver: WebDriver):
    driver.get("http://127.0.0.1:5500/pages/components/")
    span = driver.find_element(By.ID, "visibility-span")
    assert span.is_displayed(), "Span should be visible"
    driver.find_element(By.ID, "visibility-button").click()
    assert not span.is_displayed(), (
        "Span should not be visible after clicking the button"
    )


def test_display(driver: WebDriver):
    driver.get("http://127.0.0.1:5500/pages/components/")
    span = driver.find_element(By.ID, "display-span")
    assert span.is_displayed(), "Span should be visible"
    driver.find_element(By.ID, "display-button").click()
    assert not span.is_displayed(), (
        "Span should not be visible after clicking the button"
    )


def test_select(driver: WebDriver):
    driver.get("http://127.0.0.1:5500/pages/components/")
    select = Select(driver.find_element(By.ID, "dropdown"))
    select.select_by_value("option2")
    assert select.first_selected_option.text == "Option 2", (
        f"Expected 'Option 2' but got '{select.first_selected_option.text}'"
    )
    assert not select.is_multiple, "Select should not be multiple"


def test_select_multiple(driver: WebDriver):
    driver.get("http://127.0.0.1:5500/pages/components/")
    select = Select(driver.find_element(By.ID, "multi-select"))
    assert select.is_multiple, "Select should be multiple"
    selected = select.all_selected_options
    assert len(selected) == 0, "No options should be selected initially"
    select.select_by_value("option1")
    select.select_by_value("option3")
    selected = select.all_selected_options
    assert len(selected) == 2, "Two options should be selected"
    selected_texts = [option.text for option in selected]
    assert "Option 1" in selected_texts, "Option 1 should be selected"
    assert "Option 3" in selected_texts, "Option 3 should be selected"
