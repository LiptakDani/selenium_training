import uuid

from selenium.webdriver.remote.webdriver import WebDriver
import psycopg2 as psycopg

from tests.employees_page import EmployeesPage


def test_safe(driver: WebDriver):
    name = f"Test Employee {uuid.uuid4()}"[:25]
    page = EmployeesPage(driver)
    page.go()
    page.set_name(name)
    page.click_save_button()
    page.wait_for_message()
    employees = page.get_table_dictionary()
    _, names = zip(*employees)
    assert name in names, f"Employee {name} not found in the table"


def test_with_clear_database(driver: WebDriver):
    delete_employees()
    name = f"Test Employee {uuid.uuid4()}"[:25]
    page = EmployeesPage(driver)
    page.go()
    page.set_name(name)
    page.click_save_button()
    page.wait_for_message()
    employees = page.get_table_dictionary()
    _, names = zip(*employees)
    assert names == (name,), f"Expected only {name} in the table, found: {names}"

    # Clear the database after the test
    driver.execute_script("localStorage.clear();")


def delete_employees():
    with psycopg.connect(
        user="employees",
        password="employees",
        host="localhost",
        port="5432",
        database="employees",
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM employees;")
            conn.commit()
