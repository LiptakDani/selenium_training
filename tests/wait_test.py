from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_live_alert(driver: WebDriver):
    driver.get("http://127.0.0.1:5500/pages/messages/")
    driver.find_element(By.ID, "liveAlertBtn").click()

    alert = driver.find_element(By.CLASS_NAME, "alert")
    assert alert.text.startswith("Nice")


def test_delayed_alert(driver: WebDriver):
    driver.get("http://127.0.0.1:5500/pages/messages/")
    driver.find_element(By.ID, "liveAlertTimeoutBtn").click()

    wait = WebDriverWait(driver, timeout=3)
    # wait.until(lambda d: d.find_element(By.CLASS_NAME, "alert").is_displayed())
    # wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "alert")))
    # alert = driver.find_element(By.CLASS_NAME, "alert")
    # alert = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert")))
    alert = wait.until(presence_of_element_text_start_with("Nice"))

    assert alert.text.startswith("Nice")


def presence_of_element_text_start_with(prefix: str):
    def _predicate(driver: WebDriver):
        alert = driver.find_element(By.CLASS_NAME, "alert")
        text = alert.text
        if text.startswith(prefix):
            return alert
        else:
            return False

    return _predicate
