import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r":/Users/sixym3/Documents/Coding/seleniumDrivers"

class element():
    def __init__(self, driver):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.element.market/")
        self.setup_completed = False
        self.catagory = None
        
    def run_task(self):
        
        pass
        
        # time.sleep(5)
        # connect_metamask = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div[1]")
        # connect_metamask.click()

        # time.sleep(5)
        # driver.Quit()
        
    def get_listing_information(self):
        pass
        
if __name__ == "__main__":
    site = element()
    site.run_task()