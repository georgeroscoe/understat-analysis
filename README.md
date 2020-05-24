# understat-analysis

Much like the fbref analysis, I have scraped data from the excellent website https://understat.com/, which contains more advanced metrics
xG, xA, xGBuildup, and xGChain from the 2014/15 season up to and including the 2019/20 season.

understatscrape.py uses a python module to scrape all the understat data and export it in to a large csv file.

understatscatter.py produces a scatterplot of NPxG/90 versus xA/90 for each player and the corresponding season for which the data is attributed. Plot is attached in this repository.

understatchart.py produces a stacked bar chart of NPxG/90 and xA/90 for each player and the corresponding season for which the data is attributed. Plot is attached in this repository.

NPG+XA.py sums up every player's minutes, non-penalty goals, and expected assists (xA), filters out all the players with less than 7000 minutes, and also filters players below the required criteria ((NPG/90 + 3*xA/90) > 0.65). This gives us a list of the top 100 or so best attacking players from the dataset, it exports this data in to a csv file which I then analysed in R.

npgrcode.txt is a text file detailing the R code used to produce the figure NPGxA.png, which is a large plot of the dataset produced by the above python script.
