from geminiTools.job_description_parser import JobDescriptionParser
from user.userdetails import User
from user.degree import Degree
from datetime import date
from jobattributematcher.job_attribute_matcher import JobAttributeMatcher
from dotenv import load_dotenv
import os
from googlejobscraper.google_job_scraper import GoogleJobScraper

load_dotenv(".env")

descriptionParser = JobDescriptionParser(os.getenv("GEMINI_API_KEY"))
jobScraper = GoogleJobScraper(["estagio php remoto"])
jobs = jobScraper.search()
jobsJson = []

for i in jobs:
    jobsJson.append(
        descriptionParser.parseJobDescription(
            i["jobDescription"]
        )
    )

for k in enumerate(jobsJson):
    print(k)