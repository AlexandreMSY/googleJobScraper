from user.userdetails import User
from user.degree import Degree
from datetime import date
from dotenv import load_dotenv
from googlejobscraper.google_job_scraper import GoogleJobScraper
from geminiTools.job_description_to_json import JobDescriptionParser
from geminiTools.jobattributematcher.job_attribute_matcher import JobAttributeMatcher
import os

load_dotenv(".env")

jobScraper = GoogleJobScraper(["estagio php"])
jobs = jobScraper.returnJobsFound()



print(jobs)
