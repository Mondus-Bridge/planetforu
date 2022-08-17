from appium import webdriver
import pytest

@pytest.fixture
def desired_capabilities():
    desired_capabilities = {
      "platformName": "Android",
      "deviceName": "emulator-5554",
    }
    return desired_capabilities

@pytest.fixture(scope="function")
def driver(desired_capabilities):
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
    yield driver
    print("\nquit driver..")
    driver.quit()