from bs4 import BeautifulSoup
import requests
import pandas as pd

html_text = requests.get('https://www.scrapethissite.com/pages/simple/')

# print(html_text.text)

souped_html = BeautifulSoup(html_text.text, 'lxml')

# print(souped_html)

countries = souped_html.find_all("h3")

# print(countries)

for country in countries:
    print(country.text.strip())

df = pd.DataFrame([country.text.strip() for country in countries])

# print(df)

country_capitals = souped_html.find_all('span', class_='country-capital')

print(country_capitals)

for capital in country_capitals:
    print(capital.text)
