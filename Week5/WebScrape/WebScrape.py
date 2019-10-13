# Group: John Carpenter and Nathan England
# Computing ID: jmc7dt and nle4bz
# Assignment: Module 5 Web Scrapings
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import csv
site = "https://www.sports-reference.com/cbb/schools/virginia/2019-gamelogs.html"
page = urllib.request.urlopen(site)
# Use beautiful soup to make the HTML look more readable
soup = BeautifulSoup(page)
html = soup.prettify() # We can see all the HTML layed out nicely for us
table = soup.find("table")
# Use BS to clean up the HTML code
output = []
for table_row in table.findAll("tr"):
    columns = table_row.findAll("td")
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output.append(output_row)

# Write output to CSV file
with open("output.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["School" , "Virginia" , "", "", "", "", "", "", "", "", "", "", "", "", "", "" ,"","","","","","","", "Opponent"])
    writer.writerow([ "Date" , "" , "Opp" , "W/L","Points","OPP","FG","FGA","FG%","3P","3PA","3P%","FT","FTA","FT%","ORB","TRB","AST","STL","BLK","TOV","PF","",
                      "FG","FGA","FG%","3P","3PA","3P%"
                        ,"FT","FTA","FT%","ORB","TRB","AST","STL","BLK","TOV","PF"])
    writer.writerows(output)

