# Last edited on 19 May 2021
# by Rachel U. Park

"""
Status: in progress

Goal: given a url of Seabrook search criteria, returns
a List[] of available house names.
"""

from selenium import webdriver


# Option Set Up
# To Do: Set up a better systems for these options upon program start
# Maybe flags? Input options? Or a GUI?

# Set this webpage to whatever filter selections you want on Seabrook's homepage.
webpage = 'https://www.seabrookwa.com/hot-tub#fq=%7B!tag%3DRiotSolrWidget%2CRiotSolrFacetList' \
          '-sm_field_vr_featured_amenities%24name%7Dsm_field_vr_featured_amenities%24name%3A%22Dog%20Friendly%22&q' \
          '=im_field_vr_featured_amenities%24tid%3A71 '


brave_path = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
opt = webdriver.ChromeOptions()
opt.binary_location = brave_path

driver = webdriver.Chrome(options=opt)
driver.get(webpage) # Seabrook stores the search
                    # results in a div class="result-list"
resultlist = driver.find_element_by_class_name('result-list')
# print(resultlist.get_attribute('innerHTML')) # HINT
entries = resultlist.find_element_by_xpath('/html/body/div[3]/div[2]/div/main/div[2]/vrweb-search/riot-solr-container[2]/riot-solr-result-list/div/subtag[1]/div/div[2]/h4/a')
print(entries.get_attribute('innerHTML'))
