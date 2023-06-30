import os
import json
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Utils:
    def __init__(self,driver):
        #driver object
        self.driver=driver 
        #setting up logging config
        self.logger = logging.getLogger()
        log_filename=os.path.join("logs","tvo.log")
        #override old log file.
        fhandler = logging.FileHandler(filename=log_filename, mode='w')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        self.logger.addHandler(fhandler)
        self.logger.setLevel(logging.INFO)
        #explicit wait until element found
        self.logger.debug("\n getting all locators data")
        locator_path=os.path.join("utilities","locators.json")
        file=open(locator_path)
        self.locator_data=json.load(file)
        self.delay_for_explicit_wait=30
    
    #since this particaular  tests are done only docs and series page. This function is to bring initial state up. 
    def set_test_to_docs_and_series_page(self):
        self.logger.info("\n navigae to https://www.tvo.org ")
        self.driver.get("https://www.tvo.org/")
        self.logger.info("\n close the popups")
        self.explict_wait_unitl_element_found(30,By.XPATH,self.locator_data["close_popup_homepage"])
        element = self.driver.find_element("xpath",self.locator_data["close_popup_homepage"])
        element.click()
        self.logger.info("\n navigate to docs and series page")
        self.explict_wait_unitl_element_found(30,By.XPATH,self.locator_data["ds_homepage"])
        element = self.driver.find_element("xpath",self.locator_data["ds_homepage"])
        element.click()

    #explicit wait when page is taking way too long to load. 
    def explict_wait_unitl_element_found(self,delay,locator_type,locator):
        self.logger.info("\n explicit wait for the element%s"%(locator))
        element = WebDriverWait(self.driver, delay).until(
        EC.presence_of_element_located((locator_type,locator))
    )
        
    #get test data using test file and step name. 
    def get_test_data(self,test_data_file_name):
        self.logger.info("\n getting test data for the test case %s"%(test_data_file_name))
        test_file_path=os.path.join("testData",test_data_file_name+".json")
        file=open(test_file_path)
        test_data=json.load(file)
        return test_data
    
    def get_locators_data(self):
        locator_path=os.path.join("utilities","locators.json")
        file=open(locator_path)
        locator_data=json.load(file)
        return locator_data
    

        