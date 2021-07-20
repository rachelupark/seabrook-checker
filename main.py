## Last edited on 19 July 2021
## by Rachel U. Park

"""
This brief program checks the availability of a provided list of Seabrook rentals.
If a rental is available on a given date, the price and name is written to the console.

The list of house urls can either be provided in config.txt or set below as a url for
a search result.
"""

from selenium import webdriver
import time

from navtools import scroll_down
from caltools import get_av, get_price, get_name_from_url, get_search_results

### USER OPTIONS ###
# Set this webpage to whatever filter selections you want on Seabrook's homepage.
webpage = 'https://www.seabrookwa.com/hot-tub#q=im_field_vr_featured_amenities%24tid%3A71'

# Set this to the date you want checked in mm/dd format.
date = "07/08/21"

# Set this to true if you have a custom list present and want to use that instead of a given url of search results.
urlsearch = False

# Set this path to your browser binary.
brave_path = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'

######

### FIELDS ###

qualifiedhouses = []
opt = webdriver.ChromeOptions()
opt.binary_location = brave_path
driver = webdriver.Chrome(options=opt)

######

### MAIN ###

# check if user wants to use a url of search results or a list of houses in config.txt
if urlsearch:
    # Load search results and get house list.
    driver.get(webpage)
    driver.maximize_window()
    scroll_down(driver)
    qualifiedhouses = get_search_results(driver)  # hint smaller subset for testing
    print("Beginning filtering with a url of Seabrook search results...")
else:
    f = open("./config.txt", "r")
    for line in f:
        qualifiedhouses.append(line)
    print("Beginning filtering with the urls provided in config.txt...")


# loop through each house's information.
for house in qualifiedhouses:
    driver.get(house)
    isavailable = get_av(date, driver)
    housename = get_name_from_url(driver)
    if isavailable:
        print("Congrats! " + housename + " is available for check-in on " + date + "!")
        print("Here is the link: " + driver.current_url)
        print("Here is the price: " + get_price(date, driver))
    else:
        print("Sorry, " + housename + " is booked.")
print("FINISHED")

driver.quit()