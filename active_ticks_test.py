import os

os.system("pip install selenium")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
def get_active_ticks():
	driver.get("about:telemetry")
	sms = driver.find_element_by_id("simple-measurements-section")
	driver.execute_script("arguments[0].scrollIntoView(true);", sms)
	driver.execute_script("arguments[0].setAttribute('class', 'data-section has-data expanded')", sms)
	table = driver.find_element_by_id("simple-measurements")
	active_ticks = int(table.text.split("activeTicks")[1].split("\n")[0])
	return active_ticks



urls = [
	"http://www.python.org",
	"http://google.com",
	"http://facebook.com",
	"http://youtube.com",
	"http://yahoo.com",
	"http://cnn.com",
	"http://reddit.com",
	"http://gmail.com",
	"http://mozilla.org",
	"https://addons.mozilla.org"
]

for url in urls:
	print "Navigating to {}...".format(url),
	driver.get(url)
	print "scrolling to bottom"
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(6) # sleep 6 seconds, should register an active tick for every url (10)

print "\n\nactive ticks registered: {}".format(get_active_ticks())


