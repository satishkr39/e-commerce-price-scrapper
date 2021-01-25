import requests
from bs4 import BeautifulSoup
import pandas
import re
import json
import time

excel_data_df = pandas.read_excel('Details.xlsx', sheet_name='Details')
pattern = "(\d+\.\d{1,2})"
# print whole sheet data
#print(excel_data_df)

final_dict = {}
storeList = excel_data_df[' storeLink'].tolist()
for item in storeList:
    #print("==========================================")
    link = item
    print(item)
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    money = soup.find(class_="money")
    if money is None:
        money = soup.find(class_="price")
    #print("MONEY = ", money)
    #print("MONEY = ", money)
    try:
        extracted_price = re.findall(pattern, str(money))[0]
    except:
        extracted_price = None
    final_dict[item] = extracted_price

#print(len(final_dict))
print(final_dict)

# Pretty Printing JSON string back
#print(json.dumps(final_dict, indent = 4, sort_keys=True))

with open('final_report.txt', 'w') as json_file:
  json.dump(final_dict, json_file, indent = 4, sort_keys=True)

