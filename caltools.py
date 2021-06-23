## Last edited 27 May 2021
## by Rachel U. Park

# Contains tools for interacting with the Seabrook calendar on
# specific house sites.

from selenium import webdriver
import time
from navtools import scroll_down

def get_av(date: str, driver):
    # gets the overnight price of a given date
    print("Here's the given date you gave me: " + date) # HINT
    scroll_down(driver)
    mm = date.split("/")[0]

    monthdrivers = driver.find_elements_by_class_name('rcav-month')
    chosenmonthdriver = driver
    for x in monthdrivers:
        if get_mm(x) == mm:
            chosenmonthdriver = x
            break
    print("Here is the month of the driver I matched to your request:")
    print(get_mm(chosenmonthdriver))

def get_mm(monthdriver):
    monthnamedriver = monthdriver.find_element_by_class_name("rcjs-page-caption")
    monthyeararr = monthnamedriver.get_attribute('innerHTML')
    mm = month_to_mm(monthyeararr.split("&nbsp;")[0])
    return mm

def month_to_mm(month: str):
    if month == "January":
        return "01"
    elif month == "February":
        return "02"
    elif month == "March":
        return "03"
    elif month == "April":
        return "04"
    elif month == "May":
        return "05"
    elif month == "June":
        return "06"
    elif month == "July":
        return "07"
    elif month == "August":
        return "08"
    elif month == "September":
        return "09"
    elif month == "October":
        return "10"
    elif month == "November":
        return "11"
    elif month == "December":
        return "12"






