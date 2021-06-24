## Last edited 27 May 2021
## by Rachel U. Park

# Contains tools for interacting with the Seabrook calendar on
# specific house sites.

from selenium import webdriver
import time
from navtools import scroll_down

# takes a date in mm/dd/yy format and a driver for a single house's info
def get_av(date: str, driver):
    # gets the overnight price of a given date
    # print("Here's the date you gave me: " + date) #hint
    scroll_down(driver)
    mm = date.split("/")[0]
    dd = date.split("/")[1]
    yy = date.split("/")[2]

    monthdrivers = driver.find_elements_by_class_name('rcav-month')
    chosenmonthdriver = driver
    for x in monthdrivers:
        if get_mm(x) == mm:
            chosenmonthdriver = x
            break
    # print("Here is the month of the driver I matched to your request:") #hint
    # print(get_mm(chosenmonthdriver)) #hint
    # print("Here's the day I heard: " + dd) #hint
    # print("Here's the availability of the day you selected: ") #hint
    availability = get_av_day(dd, chosenmonthdriver)
    # print(availability) #hint
    if availability == "day av-O" or availability == "day av-O av-IN":
        return True
    else:
        return False

# Accepts a day and an elements object of a specific month.
def get_av_day(dd: str, monthele):
    dayele = monthele.find_elements_by_class_name('day')[int(dd)-1]
    status = dayele.get_attribute('class')
    return status

# Accepts elements object of a specific month.
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






