## Last edited on 24 June 2021
## by Rachel U. Park

"""
Status: in progress

Goal: given a url of Seabrook search criteria, returns
a List[] of available house names.
"""


from selenium import webdriver
import time

from navtools import scroll_down
from caltools import get_av

## Option Set Up
## To Do: Set up a better systems for these options upon program start
## Maybe flags? Input options? Or a GUI?

### USER OPTIONS
# Set this webpage to whatever filter selections you want on Seabrook's homepage.

webpage = 'https://www.seabrookwa.com/ocean-view#q=im_field_vr_featured_amenities%24tid%3A66'
# Set this to the date you want checked in mm/dd format.
date = "07/09/21"

#Set this path to your browser binary.
brave_path = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'

# Set up driver and load initial page results.
opt = webdriver.ChromeOptions()
opt.binary_location = brave_path

driver = webdriver.Chrome(options=opt)
driver.get(webpage)
driver.maximize_window()
scroll_down(driver)

## Functions specific to Seabrook's website

def get_name_from_url(urldriver):
    url = urldriver.current_url
    name = url.split("/")[-1]
    name = " ".join(name.split("-"))
    return name

def get_search_results(searchdriver):
    resultelements = searchdriver.find_elements_by_class_name('itemlink')
    childlinks = []

    # Populate childlinks with links to houses from search result.
    for resultlink in resultelements:
        childlinks.append(resultlink.get_attribute('href'))
    return childlinks

## Here's the program

qualifiedhouses = get_search_results(driver)[:3] #hint smaller subset for testing

for house in qualifiedhouses:
    driver.get(house)
    isavailable = get_av(date, driver)
    housename = get_name_from_url(driver)
    if isavailable:
        print("Congrats! " + driver.current_url + " is available for check-in on " + date + "!")
    else:
        print("Sorry, " + housename + " is booked.")
print("That's all she wrote, folks.")

driver.quit()