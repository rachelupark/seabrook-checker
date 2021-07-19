## Last edited on 19 July 2021
## by Rachel U. Park

"""
This brief program checks the availability of a provided list of Seabrook rentals.
If a rental is available on a given date, the price and name is written to the console.
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

if urlsearch:
    # Load search results and get house list.
    driver.get(webpage)
    driver.maximize_window()
    scroll_down(driver)
    qualifiedhouses = get_search_results(driver)  # hint smaller subset for testing
else:
    f = open("./config.txt", "r")
    for line in f:
        qualifiedhouses.append(line)

# Loop through each house's information.
for house in qualifiedhouses:
    driver.get(house)
    isavailable = get_av(date, driver)
    housename = get_name_from_url(driver)
    if isavailable:
        print("Congrats! " + driver.current_url + " is available for check-in on " + date + "!")
        print(get_price(date, driver))
    else:
        print("Sorry, " + housename + " is booked.")
print("That's all she wrote, folks.")

driver.quit()