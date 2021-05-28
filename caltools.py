## Last edited 27 May 2021
## by Rachel U. Park

from selenium import webdriver
import time

def get_price(month: str, days: List[int], html: str):
    # gets
    print(month + " " + str(days) + " " + html) # HINT