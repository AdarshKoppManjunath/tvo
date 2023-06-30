import pytest
from utilities.utils import Utils
from pages.docs_and_series_page import DocsSeriesPage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeType
from selenium import webdriver
import time
import chromedriver_autoinstaller 
chromedriver_autoinstaller.install() 


@pytest.fixture(scope='class')  
def setup(request):
    chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1200")
    chrome_options.add_argument("--ignore-certificate-errors")
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--disable-extensions")
    #chrome_options.add_argument("--no-sandbox")
    #chrome_options.add_argument("--disable-dev-shm-usage")
    request.cls.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    request.cls.util_obj =Utils(request.cls.driver)
    request.cls.util_obj.set_test_to_docs_and_series_page()
    request.cls.ds_obj= DocsSeriesPage(request.cls.driver,request.cls.util_obj)
    time.sleep(5)
    yield request.cls.driver
    request.cls.driver.close()