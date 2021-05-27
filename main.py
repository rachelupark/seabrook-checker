## Last edited on 24 May 2021
## by Rachel U. Park

"""
Status: in progress

Goal: given a url of Seabrook search criteria, returns
a List[] of available house names.
"""

from selenium import webdriver

import time

from navtools import scroll_down
from navtools import get_calendars


## Option Set Up
## To Do: Set up a better systems for these options upon program start
## Maybe flags? Input options? Or a GUI?

## Set this webpage to whatever filter selections you want on Seabrook's homepage.
webpage = 'https://www.seabrookwa.com/hot-tub#fq=%7B!tag%3DRiotSolrWidget%2CRiotSolrFacetList' \
          '-sm_field_vr_featured_amenities%24name%7Dsm_field_vr_featured_amenities%24name%3A%22Dog%20Friendly%22&q' \
          '=im_field_vr_featured_amenities%24tid%3A71 '


brave_path = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
opt = webdriver.ChromeOptions()
opt.binary_location = brave_path

driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get(webpage) # Seabrook stores the search
                    # results in a div class="result-list"
                    # The actual links to items can be found
                    # associated with their images, in <a class="itemlink" ...>
scroll_down(driver)

resultelements = driver.find_elements_by_class_name('itemlink')
childlinks = []

# populate childlinks with links to houses
for resultlink in resultelements:
    childlinks.append(resultlink.get_attribute('href'))

# go through each link
for childlink in childlinks:
    driver.get(childlink)
    print(driver.title)

driver.quit()