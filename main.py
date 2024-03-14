from googlejobscraper.googlejobscraper import GoogleJobScraper
from selenium import webdriver

test = GoogleJobScraper(searchTags=["estagio ti"])
test.search()