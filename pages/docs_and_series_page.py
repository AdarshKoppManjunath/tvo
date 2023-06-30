from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
class DocsSeriesPage:
    def __init__(self,driver,util_obj):
        self.driver=driver
        self.util_obj=util_obj
        self.locators_data=self.util_obj.get_locators_data()
        self.test_data_file_name="test_docs_series_page"
        self.test_data=self.util_obj.get_test_data(self.test_data_file_name)
        self.delay=30
    #perform all checks and store result and return it ( can be used for postive/negative). Assertion is done at the testlevel not here
    def featured_documentary_section(self): 
        try:
            #check if section present
            self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["featured_documentary_section_ds_page"])
            element = self.driver.find_element("xpath",self.locators_data["featured_documentary_section_ds_page"])
            self.util_obj.logger.info("Locator: %s selenium element: %s"%(self.locators_data["featured_documentary_section_ds_page"],element))
            return True, element
        except Exception as error:
            self.util_obj.logger.error("Error occured with the exception %s"%(error))
            return False, error
    def featured_documentary_title(self):
        #check if title correct
        try:
            title=self.locators_data["featured_documentary_title_ds_page"].replace("''","'%s'"%(self.test_data['featured_documentary_name']))
            self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,title)
            element = self.driver.find_element("xpath",title)
            self.util_obj.logger.info("Locator: %s selenium element: %s"%(title,element))
            return True, element
        except Exception as error:
            self.util_obj.logger.error("Error occured with the exception %s"%(error))
            return False, error
    def featured_documentary_description(self):
        #check if description is correct 
        try:
            description=self.locators_data["featured_documentary_description_ds_page"].replace("''","'%s'"%(self.test_data['featured_documentary_description']))
            self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,description)
            element = self.driver.find_element("xpath",description)
            self.util_obj.logger.info("Locator: %s selenium element: %s"%(description,element))
            return True, element
        except Exception as error:
            self.util_obj.logger.error("Error occured with the exception %s"%(error))
            return False, error
    def featured_documentary_play(self):
        try:
            #check "watch now" button will redirect to proper page or not.
            self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["featured_dcoumentary_play_ds_page"])
            element = self.driver.find_element("xpath",self.locators_data["featured_dcoumentary_play_ds_page"])
            self.util_obj.logger.info("Locator: %s selenium element: %s"%(self.locators_data["featured_dcoumentary_play_ds_page"],element))
            element.click()
            self.util_obj.logger.info("Current URL after redirection %s"%(self.driver.current_url))
            if self.test_data["featured_documentary_url"]   not in self.driver.current_url:
                self.driver.back()
                self.util_obj.logger.error("Error occured: %s Watch Now button link is not working"%(self.test_data["featured_documentary_url"]))
                return False, "Watch Now button link is not working"
            self.driver.back()
            return True, element
        except Exception as error:
            self.util_obj.logger.error("Error occured with the exception %s"%(error))
            return False, error
    def recently_added_title_and_respective_caption(self):
        try:
            #this function will check all the recently added videos' title and caption. Just make sure everything is added in the test data( added only 3 for the current test).
            #can be extended to link redirection check as well. 
            for data in self.test_data["recently_added_title_and_caption"]:
                title=data["title"]
                caption=data["caption"]
                title=self.locators_data["recently_added_title_ds_page"].replace("''","'%s'"%(title))
                self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,title)
                element = self.driver.find_element("xpath",title)
                self.util_obj.logger.info("Locator: %s selenium element: %s"%(title,element))
                caption=self.locators_data["recently_added_caption_ds_page"].replace("''","'%s'"%(caption))
                self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,caption)
                element = self.driver.find_element("xpath",caption)
                self.util_obj.logger.info("Locator: %s selenium element: %s"%(caption,element))
            return True,element
        except Exception as error:
            self.util_obj.logger.error("Error occured with the exception %s"%(error))
            return False, error
    def see_more_redirection_link(self):
        try:
            #this function will check for all see more redirection links on docs and series- ALL page. Test data should be updated ( added only 3 for the current test)
            for data in self.test_data["see_more_redirection_links"]:
                section_name=data["section_name"]
                redirection_link=data["redirection_link"]
                section=self.locators_data["see_more_redirection_link_ds_page"].replace("''","'%s'"%(section_name))
                self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,section)
                element = self.driver.find_element("xpath",section)
                self.util_obj.logger.info("Locator: %s selenium element: %s"%(section_name,element))
                #scroll down
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
                element.click()
                self.util_obj.logger.info("Current URL after redirection %s"%(self.driver.current_url))
                if redirection_link   not in self.driver.current_url:
                    self.driver.back()
                    self.util_obj.logger.error("Error occured: %s Redirection link is not working for %s"%(redirection_link,section_name ))
                    return False, "Redirection link is not working for %s"%(section_name)
                self.driver.back()
            return True,element
        except Exception as error:
            self.util_obj.logger.error("Error occured with the exception %s"%(error))
            return False, error
    def image_redirection_link(self):
        try:
            #this function will check for image redirection links for all sections( recently added, arts, etc) on docs and series (ALL page). Test data should be updated ( added only 3 for the current test)
            for data in self.test_data["image_redirection_links"]:
                section_name=data["section_name"]
                title=data["title"]
                redirection_link=data["redirection_link"]
                img_locator=self.locators_data["image_redirection_link_ds_page"].replace("'<section_name>'","'%s'"%(section_name))
                img_locator=img_locator.replace("'<title>'","'%s'"%(title))
                self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,img_locator)
                element = self.driver.find_element("xpath",img_locator)
                self.util_obj.logger.info("Locator: %s selenium element: %s"%(img_locator,element))
                #scroll down
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
                element.click()
                self.util_obj.logger.info("Current URL after redirection %s"%(self.driver.current_url))
                if redirection_link   not in self.driver.current_url:
                    self.driver.back()
                    self.util_obj.logger.error("Error occured: %s Redirection link is not working for %s"%(redirection_link,img_locator ))
                    return False, "Redirection link is not working for %s"%(img_locator)
                self.driver.back()
            return True,element
        except Exception as error:
            self.util_obj.logger.error("Error occured with the exception %s"%(error))
            return False, error
    
    def section_or_categories(self):
        try:
            #this function verify whether all catrgories are present or not ( test data should be updated with all the expected values, added only 3 for the current test)
            for category in self.test_data["section_or_categories"]:
                category=self.locators_data["all_section_or_categories_ds_page"].replace("''","'%s'"%(category))
                self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,category)
                element = self.driver.find_element("xpath",category)
                self.util_obj.logger.info("Locator: %s selenium element: %s"%(category,element))
            return True,element
        except Exception as error:
            self.util_obj.logger.error("Error occured with the exception %s"%(error))
            return False, error
        
        
        
          
        
          
         
         
         
        
        