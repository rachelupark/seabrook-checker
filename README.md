# Seabrook Availablity Tool by R.U.P.
A simple tool for automatically checking the overnight availability of vacation rentals on a specific day at Seabrook on short notice.

## Justification
A tool that allows for quickly checking the availability of vacation rentals at Seabrook based upon saved search criteria is necessary because of 1) the multitude of short term rentals at Seabrook, 2) the lack of an existing functionality for saving searches, and 3) the frequent occurance of unexpected cancellations which provide excellent opportunities for a low-cost, spontaneous getaway if discovered quickly.

## Usage
You can either provide a url of search results (for example: https://www.seabrookwa.com/vacation-rentals/oceanfront#q=im_field_vr_featured_amenities%24tid%3A79 ) or provide a list of urls to specific houses (for example: https://www.seabrookwa.com/vacation-rentals/second-star-right ) in config.txt. Note that each url should be a new line in config.txt. Set which option you want to use in main.py under USER OPTIONS. Make sure you also provide a path to your browser executable. 

## Behavior
Seabrook Availability Tool prints the availability of houses directly to the command line. There is no GUI.

## Compatibility
Seabrook Availability Tool only works with chromium browsers.



