from googlejobscraper.googlejobscraper import GoogleJobScraper
from selenium import webdriver

test = GoogleJobScraper(searchTags=["estagio dba"])
test.search()

f = open("test.txt", "w")

for job in test.jobsFound:
    f.write(str(job))

f.close()