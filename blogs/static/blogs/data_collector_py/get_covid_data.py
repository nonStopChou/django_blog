import bs4
import json
import time
import requests
import pandas as pd

url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
response = requests.get(url)
output = open('../covid/Taiwan_covid.xlsx', 'wb')
output.write(response.content)
output.close()

data = pd.read_csv('../covid/Taiwan_covid.xlsx')
data = data[data['location'] == 'Taiwan']
data = data[['date', 'new_cases', 'total_cases', 'new_deaths', 'total_deaths', 'new_tests', 'total_tests']]
data.to_excel('../covid/Taiwan_covid.xlsx')