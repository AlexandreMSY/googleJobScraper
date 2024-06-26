from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
import time
from googlejobscraper.containsnumber import containsNumber
from googlejobscraper.google_job_filter import GoogleJobFilter


class GoogleJobScraper(GoogleJobFilter):
    __jobsFound = {}
    __url = str("https://www.google.com/")

    def __init__(self, searchTags: list[str], filterArguments: dict = None):
        self.filterArguments = filterArguments
        self.searchTags = searchTags
        self.__driver = webdriver.Chrome()

        super().__init__(
            driver=self.__driver,
            filtersDivXpath='//*[@id="immersive_desktop_root"]/div/div[2]/div',
            filterArguments=self.filterArguments,
        )

    def returnJobsFound(self) -> dict:
        #self.__driver.minimize_window()
        for tag in self.searchTags:
            tries = 0
            
            #for some reason, google suddenly changes its layout. with enough refreshes and clearing cookies it goes back to the normal layout
            while True:
                try:
                    self.__search(tag=tag)
                #this error occurs on the new layout
                except NoSuchElementException as error:
                    #sometimes the url wont go directly to the jobs section and the program wont find the xpath below
                    if '//*[@id="choice_box_root"]/div[1]/div[1]' in error.msg:
                        if tries <= 4:
                            self.__driver.delete_all_cookies()
                            self.__driver.refresh()
                            
                            tries += 1
                        else:
                            return self.__jobsFound

                    self.__driver.delete_all_cookies()
                    self.__driver.refresh()
                    time.sleep(2)
                    pass
                else:
                    break
        return self.__jobsFound

    def __search(self, tag: str):
        self.__driver.get(
            self.__url
            + f"search?q={tag}"
            + "&ibp=htl;jobs&sa=X&ved=2ahUKEwij6a6LmKOGAxUBD7kGHRRbAtQQudcGKAF6BAgcECg&sxsrf=ADLYWIJq1flXrGqDdBp_NndzQbysd2kBnA:1716447196466#htivrt=jobs&htidocid=zVNZM09ONVexjvWhAAAAAA%3D%3D&fpstate=tldetail"
        )
        print(self.__driver.current_url)

        self.filterJobs()
        self.__getJobsListed(tagName=tag)

    def __getJobsListed(self, tagName: str = None):
        jobs = []
        scrollableJobList = self.__driver.find_element(
            By.XPATH, '//*[@id="immersive_desktop_root"]/div/div[3]/div[1]'
        )

        # the lines below are resposible for scrolling down the job list on the left side of the page

        # Get scroll height.
        last_height = self.__driver.execute_script(
            "return arguments[0].scrollHeight", scrollableJobList
        )

        # https://stackoverflow.com/questions/48850974/selenium-scroll-to-end-of-page-in-dynamically-loading-webpage
        while True:
            # Scroll down to the bottom.
            self.__driver.execute_script(
                "arguments[0].scrollTo(0, arguments[0].scrollHeight)", scrollableJobList
            )

            # Wait to load the page.
            time.sleep(2)

            # Calculate new scroll height and compare with last scroll height.
            new_height = self.__driver.execute_script(
                "return arguments[0].scrollHeight", scrollableJobList
            )

            if new_height == last_height:
                break

            last_height = new_height

            # jobWebElements = scrollableJobList.find_elements(
            #    By.TAG_NAME, "li"
            # )  # clickable elements inside the scrollable list

        jobs = scrollableJobList.find_elements(By.TAG_NAME, "li")
        jobDetails = []

        for job in jobs:
            jobDetails.append(self.__getJobDetails(job))

        self.__jobsFound[tagName] = jobDetails

    # this method scrapes the job listing attributes such as job title, company and etc
    def __getJobDetails(self, element: WebElement) -> dict:
        webdriver.ActionChains(self.__driver).move_to_element(element).click(
            element
        ).perform()

        jobDetailsDiv = self.__driver.find_element(By.ID, "tl_ditsc")

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
            if len(  # in case location text element is none
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
        jobDetailsDiv = self.__driver.find_element(By.ID, "tl_ditsc")
        shareButton = jobDetailsDiv.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/div/span/span",
        )

        webdriver.ActionChains(self.__driver).move_to_element(shareButton).click(
            shareButton
        ).perform()

        sharePopUp = self.__driver.find_element(
            By.XPATH, "/html/body/div[3]/div/div[2]/span/div"
        )

        inputFieldValue = sharePopUp.find_element(
            By.XPATH,
            "/html/body/div[3]/div/div[2]/span/div/div[3]/div[2]/div[3]/div/g-text-field/div[1]/div/input",
        ).get_attribute("value")

        closePopUpButton = self.__driver.find_element(
            By.XPATH, "/html/body/div[3]/div/div[2]/span/div/span"
        )

        time.sleep(1)  # added in order to make interactions appear more human-like

        closePopUpButton.click()

        return inputFieldValue
