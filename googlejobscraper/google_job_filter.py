from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from googlejobscraper.containsnumber import containsNumber
import time


class GoogleJobFilter:
    def __init__(
        self, driver: webdriver.Chrome, filtersDivXpath: str, filterArguments: dict = None
    ):
        self.driver = driver
        self.filtersAreaXpath = (
            filtersDivXpath  # the area where the filters buttons are located
        )
        self.isRemoteJob = False
        self.filterArguments = filterArguments

    def filterJobs(self):
        #gets buttons from the top, like 'location', 'type' etc
        filtersButtonContainer = self.driver.find_element(
            By.XPATH, '//*[@id="choice_box_root"]/div[1]/div[1]'
        )  # bar on the top that contains all the different filters (date posted, employer, etc)
        spansInsideContainer = filtersButtonContainer.find_elements(By.TAG_NAME, "span")

        for span in spansInsideContainer:
            if "cS4btb is1c5b" not in span.get_attribute("class"):
                spansInsideContainer.remove(span)

        if "Location" not in spansInsideContainer[0].text:
            self.isRemoteJob = True

        # filter arguments
        if self.filterArguments != None:
            dictKeys = list(self.filterArguments) #extract dict keys
            locationMaxDistance = None
            maxDatePosted = None
            
            if 'locationMaxDistance' in dictKeys:
                locationMaxDistance = self.filterArguments["locationMaxDistance"]
            
            if 'maxDatePosted' in dictKeys:
                maxDatePosted = self.filterArguments["maxDatePosted"]

            # the spans are acting as buttons
            for button in spansInsideContainer:
                if "Location" in button.text:
                    button.click()
                    
                    if locationMaxDistance != None:
                        self.__setLocationMaxDistance(locationMaxDistance)
                        
                elif "Date posted" in button.text:
                    button.click()
                    
                    if maxDatePosted != None:
                        self.__setMaxDatePosted(maxDatePosted)
                        
                elif "New to you" in button.text:
                    button.click()
                elif "Type" in button.text:
                    button.click()
                    # self.__setJobType(2)
                else:
                    button.click()

    # returns the filter clickable buttons inside the filter area on the top of the page
    # https://imgur.com/fjUTSlP
    def __getButtonsInsideContainer(
        self,
        isRemoteJob: bool,
        xpath: str,
        remoteXpath: str,  # for some reason the container xpath if the job being searched for is a remote job
        buttonDivClass: str,
    ) -> list[WebElement]:
        buttonsContainer = self.driver.find_element(
            By.XPATH, xpath if isRemoteJob else remoteXpath
        )
        divsInsideContainer = buttonsContainer.find_elements(By.TAG_NAME, "div")

        # filter divs that arent buttons
        # still not filtering placeholders, but i think its good enough
        for div in divsInsideContainer:
            if buttonDivClass in div.get_attribute("class"):
                if len(div.text) < 1:
                    divsInsideContainer.remove(div)
            else:
                divsInsideContainer.remove(div)

        return divsInsideContainer

    def __setLocationMaxDistance(self, buttonIndex: int):
        buttons = self.__getButtonsInsideContainer(
            isRemoteJob=self.isRemoteJob,
            xpath='//*[@id="choice_box_root"]/div[2]/div[1]/div[1]',
            remoteXpath='//*[@id="choice_box_root"]/div[2]/div[1]/div[1]',
            buttonDivClass="TRwkpf GbaVB",
        )

        if buttonIndex <= len(buttons):
            buttons[buttonIndex].click()
        else:
            buttons[len(buttons)].click()

    def __setMaxDatePosted(self, buttonIndex: int):
        buttons = self.__getButtonsInsideContainer(
            isRemoteJob=self.isRemoteJob,
            xpath='//*[@id="choice_box_root"]/div[2]/div[1]/div[2]',
            remoteXpath='//*[@id="choice_box_root"]/div[2]/div[2]/div[2]',
            buttonDivClass="eNr05b",
        )

        if buttonIndex <= len(buttons):
            buttons[buttonIndex].click()
        else:
            buttons[len(buttons)].click()

    # to be implemented
    def __setNewToYou(self, buttonIndex: int):
        pass

    # not working yet
    # function not finding the buttons
    def __setJobType(self, buttonIndex: int):
        buttons = self.__getButtonsInsideContainer(
            isRemoteJob=self.isRemoteJob,
            xpath='//*[@id="choice_box_root"]/div[2]/div[3]',
            remoteXpath='//*[@id="choice_box_root"]/div[2]/div[2]',
            buttonDivClass="GbaVB",
        )

        for i in buttons:
            print(i.text)
