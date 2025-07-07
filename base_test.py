import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.environment_verification import is_emulator_online

options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "emulator-5554"
options.app_package = "com.android.settings"
options.app_activity = ".Settings"

appium_server_url = 'http://localhost:4723/wd/hub'


@pytest.fixture(scope="function")
def driver(request):
    driver = webdriver.Remote(appium_server_url, options=options)

    if not is_emulator_online('localhost'):
        pytest.fail("Emulator is not online, aborting test.")

    def fin():
        if driver:
            driver.quit()

    request.addfinalizer(fin)

    return driver

def test_find_do_not_disturb(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "com.android.settings:id/homepage_container")))
    el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Do Not Disturb, Bedtime"]')
    el.click()
