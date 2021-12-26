# Import the pandas library
import pandas as pd
# Import seaborn to help create more visually appealing plots; see https://seaborn.pydata.org/introduction.html#introduction for more information
import seaborn as sns
from matplotlib import pyplot as plt


# Read the data from a csv file and save it as a pandas dataframe named 'xg_data'
# Replace the file path with the location on your computer where the csv file is saved (in my case it's in D:/Tom/Downloads/)
xg_data = pd.read_csv('C:/PycharmProjects/FantasyPL/table.csv')

xg_data['GD/90'] = xg_data['GD'] / xg_data['MP']
xg_data['GDxGDifference'] = xg_data['GD/90'] - xg_data['xGD/90']
xg_data['PPG'] = xg_data['Pts'] / xg_data['MP']


# Order the teams by NPxGD to help give an idea of who the good and bad teams are currently
xg_data = xg_data.sort_values(by=['PPG'], ascending=False)

# Create a horizontal bar chart to help visualise the teams that have been overperforming or underperforming in terms of GD vs xGD
#plt.barh(xg_data['Squad'], xg_data['GDxGDifference'])

# Show the plot
#plt.show()


# Set the plot style and colour palette to use (remember dodgy spelling if you're from the UK!)
sns.set(style='whitegrid')
sns.set_color_codes('muted')

# Initialize the matplotlib figure (f) and axes (ax), and set width and height of the plot
f, ax = plt.subplots(figsize=(12, 10))

# Create the plot, choosing the variables for each axis, the data source and the colour (b = blue)
sns.barplot(x='GDxGDifference', y='Squad', data=xg_data, color='b')

# Rename the axes, setting y axis label to be blank
ax.set(ylabel='', xlabel='Difference in GD vs xGD')

# Remove the borders from the plot
sns.despine(left=True, bottom=True)

plt.show()
