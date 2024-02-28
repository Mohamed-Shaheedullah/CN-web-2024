from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl


html_text = requests.get('https://www.scrapethissite.com/pages/simple/')

# print(html_text.text)

souped_html = BeautifulSoup(html_text.text, 'lxml')

# print(souped_html)

countries = souped_html.find_all("h3")

# print(countries)

countries_list = []

for country in countries:
    countries_list.append(country.text.strip())

# df = pd.DataFrame([country.text.strip() for country in countries])

# print(df)

country_capitals = souped_html.find_all('span', class_='country-capital')

# print(country_capitals)

capitals = []

for capital in country_capitals:
    capitals.append(capital.text.strip())

country_pop = souped_html.find_all('span', class_='country-population')

populations = []

for pop in country_pop:
    populations.append(pop.text.strip())

# print(countries_list)
# print(capitals)
# print(populations)

country_areas = souped_html.find_all('span', class_='country-area')

areas =[]
for area in country_areas:
    areas.append(area.text.strip())

# print(areas)

my_dict = {}
my_dict["country"] = countries_list
my_dict["capital"] = capitals
my_dict["population"] = populations
my_dict["Area"] = areas

# print(my_dict)

df = pd.DataFrame(my_dict)

print(df.head())
df.to_excel("countries.xlsx", index=False)
