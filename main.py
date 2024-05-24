from datetime import date
from dotenv import load_dotenv
from googlejobscraper.google_job_scraper import GoogleJobScraper
from geminiTools.job_description_to_json import JobDescriptionParser
from geminiTools.jobattributematcher.job_attribute_matcher import JobAttributeMatcher
import os
from tomlTools.create_toml import createToml
from tomlTools.read_toml import readToml

createToml()
toml = readToml("./config.toml")

load_dotenv(".env")

jobScraper = GoogleJobScraper(
    ["estágio php", "estágio javascript", "estágio front-end"],
    {
        "locationMaxDistance": toml["GOOGLE"]["location_max_distance"],
        "maxDatePosted": toml["GOOGLE"]["max_date_posted"],
    },
)

jobs = jobScraper.returnJobsFound()

print(jobs)
