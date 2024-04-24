# import requests
# import json

# url = 'https://raw.githubusercontent.com/awasekhirni/jsondata/master/100books.json'
# response = requests.get(url)
# data = response.json()
# # print(data)

# countries = list({i['country'] for i in data})
# # print(countries)
# # print(len(countries))

# newDict = {}
# for i in data:
#     for j in countries:
#         if j == i['country']:
#             newDict.setdefault(j, []).append(i['title'])
        
# print(newDict)

# json_object = json.dumps(newDict, indent=2)


# with open("data.json", "w") as file:
#     file.write(json_object)

#------------------------------------------------------------------------------------------------------------------------------------------
# import pandas as pd

# url = 'https://raw.githubusercontent.com/awasekhirni/jsondata/master/100books.json'
# dataset = pd.read_json(url)
# print(dataset.head())

# country = dataset['country']
# print(country)

#------------------------------------------------------------------------------------------------------------------------------------------

# x = [1, 2, 3, 4, 5]
# y = x.copy()
# x.append(10)
# print(y)
# print(x)

# mystr = "apple"
# myit = iter(mystr)

# print(next(myit))

# print(next(myit))