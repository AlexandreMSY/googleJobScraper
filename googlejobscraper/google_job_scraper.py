from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time
from googlejobscraper.containsnumber import containsNumber
from selenium.webdriver.support.wait import WebDriverWait


class GoogleJobScraper:
    jobsFound = []
    url = str("https://www.google.com/")
    driver = webdriver.Chrome()

    def __init__(self, searchTags: list[str]):
        self.searchTags = searchTags

    def search(self) -> list:
        for tag in self.searchTags:
            self.driver.get(self.url + f"/search?q={tag}")
            if self.__isJobRelatedTag():
                self.__getJobsListed()
            else:
                print("not job related")

        return self.jobsFound

    # checks if search tag is a job related tag
    def __isJobRelatedTag(self) -> bool:
        jobsQuickResult = self.driver.find_elements(By.CLASS_NAME, "nJXhWc")
        arrayLength = len(jobsQuickResult)

        return True if arrayLength > 0 else False

    def __getJobsListed(self):
        moreJobsButton = self.driver.find_element(By.CLASS_NAME, "esVihe")
        moreJobsButton.click()

        scrollableJobList = self.driver.find_element(
            By.XPATH, '//*[@id="immersive_desktop_root"]/div/div[3]/div[1]'
        )
        jobWebElements = []

        # the lines below are resposible for scrolling down the job list on the left side of the page

        # Get scroll height.
        last_height = self.driver.execute_script(
            "return arguments[0].scrollHeight", scrollableJobList
        )

        # https://stackoverflow.com/questions/48850974/selenium-scroll-to-end-of-page-in-dynamically-loading-webpage
        while True:
            # Scroll down to the bottom.
            self.driver.execute_script(
                "arguments[0].scrollTo(0, arguments[0].scrollHeight)", scrollableJobList
            )

            # Wait to load the page.
            time.sleep(2)

            # Calculate new scroll height and compare with last scroll height.
            new_height = self.driver.execute_script(
                "return arguments[0].scrollHeight", scrollableJobList
            )

            if new_height == last_height:
                break

            last_height = new_height

            jobWebElements = scrollableJobList.find_elements(
                By.TAG_NAME, "li"
            )  # clickable elements inside the scrollable list

        for element in jobWebElements:
            jobDetails = self.__getJobDetails(element)
            self.jobsFound.append(jobDetails)

        self.driver.close()

    # this method scrapes the job listing attributes such as job title, company and etc
    def __getJobDetails(self, element: WebElement) -> dict:
        webdriver.ActionChains(self.driver).move_to_element(element).click(
            element
        ).perform()

        jobDetailsDiv = self.driver.find_element(By.ID, "tl_ditsc")
        jobTitle = jobDetailsDiv.find_element(By.TAG_NAME, "h2").text
        company = jobDetailsDiv.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div[2]/div[1]",
        ).text
        location = (
            jobDetailsDiv.find_elements(
                By.XPATH,
                "/html/body/div[2]/div/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div[2]/div[2]",
            )[0].text
            if len(                              #in case location text element is none
                jobDetailsDiv.find_elements(
                    By.XPATH,
                    "/html/body/div[2]/div/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div[2]/div[2]",
                )
            )
            > 0
            else ""
        )
        timePosted = None
        contractDetailsDiv = jobDetailsDiv.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div/div/div[3]",
        ).find_elements(By.CLASS_NAME, "LL4CDc")
        contractDetails = {"salary": None, "contractType": None}

        jobDescriptionDiv = jobDetailsDiv.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div/div/div[4]",
        )

        showFullDescriptionButton = jobDescriptionDiv.find_elements(
            By.XPATH,
            "/html/body/div[2]/div/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div/div/div[4]/div/div/div/div/g-expandable-content/span/div/g-inline-expansion-bar/div[1]/div",
        )

        # if show full description button exists
        if len(showFullDescriptionButton) > 0:
            showFullDescriptionButton[0].click()

        for element in contractDetailsDiv:
            if containsNumber(element.text):
                if (
                    "ago" in element.text
                ):  # checks if string contains the word ago as in 9 months ago
                    timePosted = element.text
                else:
                    contractDetails["salary"] = element.text
            else:
                contractDetails["contractType"] = element.text

        return {
            "jobTitle": jobTitle,
            "company": company,
            "location": location,
            "timePosted": timePosted,
            "contractDetails": contractDetails,
            "jobDescription": jobDescriptionDiv.text,
            "url": self.__getShareLink(),
        }

    def __getShareLink(self) -> str:
        jobDetailsDiv = self.driver.find_element(By.ID, "tl_ditsc")
        shareButton = jobDetailsDiv.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/div/span/span",
        )

        webdriver.ActionChains(self.driver).move_to_element(shareButton).click(
            shareButton
        ).perform()

        sharePopUp = self.driver.find_element(
            By.XPATH, "/html/body/div[3]/div/div[2]/span/div"
        )

        inputFieldValue = sharePopUp.find_element(
            By.XPATH,
            "/html/body/div[3]/div/div[2]/span/div/div[3]/div[2]/div[3]/div/g-text-field/div[1]/div/input",
        ).get_attribute("value")

        closePopUpButton = self.driver.find_element(
            By.XPATH, "/html/body/div[3]/div/div[2]/span/div/span"
        )

        time.sleep(1)  # added in order to make interactions appear more human-like

        closePopUpButton.click()

        return inputFieldValue
