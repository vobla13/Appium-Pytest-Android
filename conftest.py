import os
import pytest
from appium import webdriver
from proxy.bmp_proxy import ProxyManager


EXECUTOR = '0.0.0.0:4723/wd/hub'
TARGET_ANDROID_APP = os.path.abspath('apps/Chess_v3.56_apkpure.com.apk')

ANDROID_BASE_CAPS = {
    'app': TARGET_ANDROID_APP,
    'automationName': 'UIAutomator2',
    'platformName': 'Android',
    'platformVesion': os.getenv('ANDROID_PLATFORM_VERSION') or '10.0',
    'deviceName': os.getenv('ANDROID_DEVICE_NAME') or 'Pixel',
    'newCommandTimeout': '1800',
    'clearDeviceLogsOnStart': True
}


@pytest.fixture
def mobile_driver(request):

    driver = webdriver.Remote(EXECUTOR, ANDROID_BASE_CAPS)
    yield driver
    driver.quit()


