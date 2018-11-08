# Py_Data_Miner
Python data miner using selenium web-driver. This uses the headless version of Seleniums chrome driver in order to search the Steam users list for player information after it has been dynamically generated. After the data has been grabbed, then BeatifulSoup is used to find the the correct data in the html that I'm looking for.

Currently the script only works for one page, but will later be expanded to loop through a given number of pages. I created this in order to mine data from the Steam website, but later foundout that it's unnecessary to do so because their API gives out that information already. May revisit using their API instead.
