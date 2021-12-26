import requests
from bs4 import BeautifulSoup
import csv

output_file = csv.writer(open('prem_table_bs.csv', 'w'))
#w allows python to write to the file

output_file.writerow(['Rk', 'Squad', 'MP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts', 'xG', 'xGA', 'xGD', 'xGD/90'])

result = requests.get("https://fbref.com/en/comps/9/Premier-League-Stats")

src = result.content

soup = BeautifulSoup(src, 'html.parser')

#Finds all the tables
table = soup.find_all("table")
league_table = table[0]
teams = league_table.find_all("tr")

for team in teams[1:21]:

    stats = team.find_all("td")

    Rk = stats[0].text
    Squad = stats[2].text
    MP = stats[3].text
    W = stats[4].text
    D = stats[5].text
    L = stats[6].text
    GF = stats[7].text
    GA = stats[8].text
    GD = stats[9].text
    Pts = stats[10].text
    xG = stats[11].text
    xGA = stats[12].text
    xGD = stats[13].text
    xGD90 = stats[14].text

output_file.writerow([Rk, Squad, MP, W, D, L, GF, GA, GD, Pts, xG, xGA, xGD, xGD90])


