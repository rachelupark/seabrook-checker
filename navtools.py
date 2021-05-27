# Last edited 24 May 2021
# by Rachel U. Park

"""
Scrolls down to bottom of webpage so all house
options load!

Got this solution from
https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
answer author: OWADVL
"""

from selenium import webdriver
import time

SCROLL_PAUSE_TIME = 2.0 # number of seconds to pause before scrolling further

# scolls up and down the page to trigger loading of content
def scroll_down(driver):
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Scroll back up a bit so the listings load
        driver.execute_script("window.scrollTo(0, 3500);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height










