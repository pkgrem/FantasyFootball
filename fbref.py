# Import the pandas library
import pandas as pd

# Read the data from a csv file and save it as a pandas dataframe named 'xg_data'
# Replace the file path with the location on your computer where the csv file is saved (in my case it's in D:/Tom/Downloads/)
xg_data = pd.read_csv('D:/Tom/Downloads/epl_xg.csv')

# Take a look at the data
print(xg_data)