# Group: John Carpenter and Nathan England
# Computing ID: jmc7dt and nle4bz
# Assignment: Module 5 Web Scrapings
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

csv_read = pd.read_csv(r"C:\Users\jmcarpenter\Desktop\UVA Graduate School Stuff\CS_DataScience_5010\CS_5010\Week5\WebScrape\output.csv" , sep=',',encoding='latin1')
keys = csv_read.keys()
# We want to first clean the data by dropping the rows have NA's in them.
clean_data=csv_read.dropna(how='all')
# Drop the first row of the data
print(clean_data)
# Lets show how the number of points scored for Virginia changed over the year )
# First we grab the opp
opp = clean_data["Unnamed: 2"].iloc[1:]

# Then grab the total points scored for virginia in each game
va_points_scored = np.array(clean_data["Unnamed: 4"].iloc[1:]) # These are stored as strings and we want to fix this
# Fixing the scores as integers
va_points_scored = va_points_scored.astype(int)
# opponents scores at each game
opponent_scores = np.array(clean_data["Unnamed: 5"].iloc[1:])
# convert opponent scores to int
opponent_scores = opponent_scores.astype(int)
# Plotting the number of Points scored in the each game by virginia
plt.bar(opp,va_points_scored,width=0.8,color="r")
plt.bar(opp,opponent_scores,width=0.8,color="b")
plt.xticks(rotation = 70)
plt.title("Virginia Margin Over Opponents")
plt.legend(["Virginia Points","Opponent Points"])
plt.ylabel("Margin of Victory")
plt.show()

# We want to know the proportion of 3pointers to 2pointers made during the year
# First we get the total number of  points scored throughout the year and divide by the number of
total_points = np.sum(va_points_scored) # 2714
# Get three pts made in each game
three_pts = clean_data["Unnamed: 9"].iloc[1:] # Need to convert to a string
# Get the summary stats of Three pts
# convert to int
three_pts_convert = three_pts.astype(int)
print("Summary statistics of 3 pointers:")
print(three_pts_convert.describe())
# convert to string
three_pts = np.sum(np.array(three_pts.astype(int))) # Multiply 3 times the number of 3 pointers made
total_three_pts = 3*three_pts
#
print("The Number of Three Pointers Made Last Season: ",three_pts)
# Get the ammount of points made that are three pointers
print("Points scored from 3 pointers last season: ",total_three_pts)
# The proporportion of total points scored throughout the season in relationship to three pointers
three_pts_to_total_pts = total_three_pts / total_points * 100
print("Percent of total points that were 3pts: {}%".format(round(three_pts_to_total_pts,2))) # Use round operator to carry to 2 decimal places
# Get summary statistics on the data
# Free throw percentage analysis
ftp = np.array(clean_data["Unnamed: 14"].iloc[1:].astype(float) )
#
print("Number of games where the FT% was greater than 75%: ",len(np.where(ftp > .75)[0]))
# Find which teams defended against VA three point offense
three_pointers = np.array( three_pts_convert)
plt.bar(opp , three_pointers,width=0.8,color="b")
plt.title("Number of 3pts VS Opponent")
plt.xticks(rotation=70)
plt.ylabel("3pts Made")
plt.xlabel("Opponent")
plt.show()




























