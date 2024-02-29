from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl

html_text = requests.get('https://wearecodenation.com/2024/01/23/data-course-playground/').text

# print(html_text)

soup = BeautifulSoup(html_text, 'lxml')

# print(soup)

# <h5 class="elementor-heading-title elementor-size-default">Level 4: Apprenticeship: Software Developer</h5>

h5s = soup.find_all('h5', class_="elementor-heading-title elementor-size-default")

my_dict ={}

## this segment prints all of the course titles

for h5 in h5s:
    if ":" in h5.text:
        my_dict[h5.text] = ""
        # print(h5.text)

# print(my_dict)



h6s=soup.find_all("h6")

# for h6 in h6s:
#     print(h6.text)


# for h5 in h5s:
#     if ":" in h5.text:
#         h6_match = h5.find_next('h6')
#         for single_date in h6_match.strings:
#             pass
#             # print(single_date)
        


my_dict ={}

# for h5 in h5s:
#     if ":" in h5.text:
#         h6_match = h5.find_next('h6')
#         # print(h5.text)
#         for single_date in h6_match.strings:
#             my_dict[h5.text] = single_date
#                 # print(single_date)

# print(my_dict)


all_dates = []

for h5 in h5s:
    if ":" in h5.text:
        my_dict[h5.text] = ""
        h6_match = h5.find_next('h6')
        # print(h5.text)
        for single_date in h6_match.strings:
            all_dates.append(single_date)
            print(h5.text)
            print(single_date)
            for key in my_dict.keys():
                if  key == h5.text:
                    my_dict[key] = single_date

print(my_dict)