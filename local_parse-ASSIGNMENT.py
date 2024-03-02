from bs4 import BeautifulSoup
import requests
import pandas as pd

with open("index.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    

title_list =[]

lists = soup.find_all('ol')

titles = soup.find_all( 'h3', class_='favourites' )

for my_title in titles:
    title_list.append(my_title.text)

first_place = []
second_place = []
third_place = []


for list_item in lists:
    first_element = list_item.find('li') 
    if first_element:
        first_place.append(first_element.text)
        # print(first_element.text)

# use indexing, check and loop
# https://stackoverflow.com/questions/8724352/getting-the-nth-element-using-beautifulsoup

for list_item_2 in lists:  # remember lists is all ol
    all_list_items = list_item_2.find_all('li')  # Find all <li> items within ol
    if len(all_list_items) >= 2:  # Check if there's a second item
        second_element = all_list_items[1]  # use indexing to find element
        second_place.append(second_element.text)
        # print(second_element.text)


for list_item_3 in lists:
    all_list_items = list_item_3.find_all('li')  
    if len(all_list_items) >= 3:  
        third_element = all_list_items[2]
        third_place.append(third_element.text)
        # print(third_element.text)

## alternative method that works.
# https://stackoverflow.com/questions/24720442/selecting-second-child-in-beautiful-soup-with-soup-select/44509934

# element = soup.select( "#hobbies > li:nth-child(2)" )
# print(element)



my_dict = {}
my_dict["Titles"] = title_list
my_dict["First Place"] = first_place
my_dict["Second Place"] = second_place
my_dict["Third Place"] = third_place

# print(my_dict)

df = pd.DataFrame(my_dict)
print(df)

df.to_excel("favourites.xlsx", index=False)

