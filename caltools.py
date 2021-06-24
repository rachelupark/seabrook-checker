## Last edited 24 June 2021
## by Rachel U. Park

# Contains tools for interacting with the Seabrook calendar on
# specific house sites.

from selenium import webdriver
import time
from navtools import scroll_down

# accepts a date in mm/dd format and a driver for a single house's info
# returns whether the house is available on that day
def get_av(date: str, driver):
    scroll_down(driver)
    mm = date.split("/")[0]
    dd = date.split("/")[1]

    monthdrivers = driver.find_elements_by_class_name('rcav-month')
    chosenmonthdriver = driver
    for x in monthdrivers:
        if get_mm(x) == mm:
            chosenmonthdriver = x
            break

    availability = get_av_day(dd, chosenmonthdriver)

    if availability == "day av-O" or availability == "day av-O av-IN":
        return True
    else:
        return False

def get_price(date: str, driver):
    # return the price of that night as an int
    return


######################################################################
## These methods are only for caltools. Please don't import them.

def find_month(date, driver):
    # return web elements corresponding to the selected month.
    return


# Accepts a day and an elements object of a specific month.
def get_av_day(dd: str, monthele):
    dayele = monthele.find_elements_by_class_name('day')[int(dd)-1]
    status = dayele.get_attribute('class')
    return status

def get_price_day(dd: str, monthele):
    dayele = monthele.find_elements_by_class_name('rc-price')[int(dd)-1]
    price = dayele.get_attribute('innerHTML')
    price = "".join(price[1:].split(","))
    return int(price)

# Accepts elements object of a specific month.
def get_mm(monthdriver):
    monthnamedriver = monthdriver.find_element_by_class_name("rcjs-page-caption")
    monthyeararr = monthnamedriver.get_attribute('innerHTML')
    mm = month_to_mm(monthyeararr.split("&nbsp;")[0])
    return mm


## Simple formatting and conversion methods.
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






