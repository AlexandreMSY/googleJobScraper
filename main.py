from googlejobscraper.googlejobscraper import GoogleJobScraper
from selenium import webdriver

test = GoogleJobScraper(searchTags=["programador junior remoto"])
test.search()