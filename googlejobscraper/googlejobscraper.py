from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from typing import Type
from user.userdetails import UserDetails
import time


class GoogleJobScraper:
    url = str("https://www.google.com/")
    driver = webdriver.Chrome()

    def __init__(self, searchTags: list[str]):
        self.searchTags = searchTags

    def search(self):
        for tag in self.searchTags:
            self.driver.get(self.url + f"/search?q={tag}")
            if self.__isJobRelatedTag():
                self.__getJobList()
            else:
                print("not job related")

            while True:
                pass

    # checks if search tag is a job related tag
    def __isJobRelatedTag(self) -> bool:
        jobsQuickResult = self.driver.find_elements(By.CLASS_NAME, "nJXhWc")
        arrayLength = len(jobsQuickResult)

        return True if arrayLength > 0 else False

    def __getJobList(self):
        moreJobsButton = self.driver.find_element(By.CLASS_NAME, "esVihe")
        moreJobsButton.click()

        foundJobsList = self.driver.find_element(
            By.XPATH, '//*[@id="immersive_desktop_root"]/div/div[3]/div[1]'
        )
        last_height = self.driver.execute_script(
            "return arguments[0].scrollHeight", foundJobsList
        )

        #https://stackoverflow.com/questions/48850974/selenium-scroll-to-end-of-page-in-dynamically-loading-webpage
        while True:
            self.driver.execute_script(
                "arguments[0].scrollTo(0, arguments[0].scrollHeight)", foundJobsList
            )
            time.sleep(2)
            new_height = self.driver.execute_script(
                "return arguments[0].scrollHeight", foundJobsList
            )

            if new_height == last_height:
                break

            last_height = new_height
            
        print(len(foundJobsList.find_elements(By.TAG_NAME, "li")))
