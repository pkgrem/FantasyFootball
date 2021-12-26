import pandas as pd
import requests
from bs4 import BeautifulSoup, Comment
import csv

output_file = csv.writer(open('prem_table_bs.csv', 'w'))
#w allows python to write to the file

output_file.writerow(['Rk', 'Squad', 'MP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts', 'xG', 'xGA', 'xGD', 'xGD/90'])


url = 'https://fbref.com/play-index/share.fcgi?id=ALSaw'
response = requests.get(url)

tables = pd.read_html(response.text, header=0)

# Get the tables within the Comments
soup = BeautifulSoup(response.text, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for each in comments:
    if 'table' in str(each):
        try:
            table = pd.read_html(str(each), header=1)[-1]
            table = table[table['Rk'].ne('Rk')].reset_index(drop=True)
            tables.append(table)
        except:
            continue

for table in tables:
   # print(table['Rk'])


    Rk = table['Rk']
    Squad = table['Squad']
    MP = table['MP']
    W = table['W']
    D = table['D']
    L = table['L']
    GF = table['GF']
    GA = table['GA']
    GD = table['GD']
    Pts = table['Pts']
    xG = table['xG']
    xGA = table['xGA']
    xGD = table['xGD']
    xGD90 = table['xGD/90']


output_file.writerow([Rk, Squad, MP, W, D, L, GF, GA, GD, Pts, xG, xGA, xGD, xGD90])