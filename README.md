# understat-analysis

Much like the fbref analysis, I have scraped data from the excellent website https://understat.com/, which contains more advanced metrics
xG, xA, xGBuildup, and xGChain from the 2014/15 season up to and including the 2019/20 season.

understatscrape.py uses a python module to scrape all the understat data and export it in to a large csv file.

understatscatter.py produces a scatterplot of NPxG/90 versus xA/90 for each player and the corresponding season for which the data is attributed.

understatchart.py produces a stacked bar chart of NPxG/90 and xA/90 for each player and the corresponding season for which the data is attributed.

I have attached both the produced images in this repository.
