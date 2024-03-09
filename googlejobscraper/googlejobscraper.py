from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from typing import Type
from user.userdetails import UserDetails
import time

class GoogleJobScraper:
    url = str("https://www.google.com/")
    driver = webdriver.Chrome()
    
    def __init__(self, searchTags : list[str]):
        self.searchTags = searchTags
    
    def search(self):
        for tag in self.searchTags:
            self.driver.get(self.url + f"/search?q={tag}")
            print(
                self.__isJobRelatedTag()
            )
            time.sleep(3)
    
    #checks if search tag is a job related tag
    def __isJobRelatedTag(self) -> bool:
        jobsQuickResult = self.driver.find_elements(By.CLASS_NAME, "nJXhWc")
        arrayLength = len(jobsQuickResult)
        
        return True if arrayLength > 0 else False
        