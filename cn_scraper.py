from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl
import collections

html_text = requests.get('https://wearecodenation.com/2024/01/23/data-course-playground/').text


soup = BeautifulSoup(html_text, 'lxml')

h5s = soup.find_all('h5', class_="elementor-heading-title elementor-size-default")

# my_dict ={}

# for h5 in h5s:
#     if ":" in h5.text:
#         my_dict[h5.text] = ""
#         # print(h5.text)

# print(my_dict)


h6s = soup.find_all("h6")

# for h6 in h6s:
#     print(h6.text)


# for h5 in h5s:
#     if ":" in h5.text:
#         h6_match = h5.find_next('h6')
#         for single_date in h6_match.strings:
#             pass
#             # print(single_date)
        


# my_dict ={}

# for h5 in h5s:
#     if ":" in h5.text:
#         h6_match = h5.find_next('h6')
#         # print(h5.text)
#         for single_date in h6_match.strings:
#             my_dict[h5.text] = single_date
#                 # print(single_date)

# print(my_dict)

my_dict = collections.defaultdict(list)

for h5 in h5s:
    if ":" in h5.text:
        h6_match = h5.find_next('h6')
        # print(h5.text)
        for single_date in h6_match.strings:
            print(h5.text)
            print(single_date)
            my_dict[h5.text].append(single_date)
            # my_dict[h5.text] = single_date

df = pd.DataFrame(dict([(key, pd.Series(value)) for key, value in my_dict.items()]))

print(df)

# df2 = pd.DataFrame(my_dict)
# print(df2)
