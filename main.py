from geminiTools.job_description_to_json import JobDescriptionToJson
from user.userdetails import User
from user.degree import Degree
from datetime import date
from jobattributematcher.job_attribute_matcher import JobAttributeMatcher
from dotenv import load_dotenv
from googlejobscraper.google_job_scraper import GoogleJobScraper
import os

load_dotenv(".env")

jobScraper = GoogleJobScraper(["estágio php remoto"])
jobs = jobScraper.returnJobsFound()

jsonCreator = JobDescriptionToJson(os.getenv("GEMINI_API_KEY"))
jobJSON = jsonCreator.createJson(
    jobs["estágio php remoto"][0]["jobDescription"]
)

print(jobJSON)
