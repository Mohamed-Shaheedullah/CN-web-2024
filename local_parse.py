from bs4 import BeautifulSoup
import requests
import pandas as pd

with open("index.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    

# print(soup)

# first_fav = soup.find_all('section', class_='Favourites')

# print(first_fav)

lists = soup.find_all('ul')

titles = soup.find_all('ul')

# for my_title in titles:
#     my_title.decompose()
#     print(my_title.text)

first_place = []
second_place = []
third_place = []

for list_item in lists:
    first_element = list_item.find('li') 
    if first_element:
        first_place.append(first_element.text)
        # print(first_element.text)

from bs4 import BeautifulSoup

# ... (Your HTML and initial setup code is the same) ...

for list_item_2 in lists:
    all_list_items = list_item_2.find_all('li')  # Find all <li> items
    if len(all_list_items) >= 2:  # Check if there's a second item
        second_element = all_list_items[1]
        second_place.append(second_element.text)
        # print(second_element.text)


for list_item_3 in lists:
    all_list_items = list_item_3.find_all('li')  # Find all <li> items
    if len(all_list_items) >= 3:  # Check if there's a third item
        third_element = all_list_items[2]
        third_place.append(third_element.text)
        # print(third_element.text)


# print(second_place)


# row = 5
# while true
#     element = soup.select('tr:nth-of-type('+ row +')')
#     if len(element) > 0:
#         # element is your desired row element, do what you want with it 
#         row += 5
#     else:
#         break

