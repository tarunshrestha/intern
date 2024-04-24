import requests
import json

url = 'https://raw.githubusercontent.com/awasekhirni/jsondata/master/100books.json'
response = requests.get(url)
data = response.json()
# print(data)

countries = list({i['country'] for i in data})
# print(countries)
# print(len(countries))

newDict = {}
# To add in new dictionary
for i in data:
    for j in countries:
        if j == i['country']:
            newDict.setdefault(j, []).append(i)
            
# To remove country from new dict
for i in newDict:
    for j in newDict[i]:
            j.pop('country')

print(newDict)

json_object = json.dumps(newDict, indent=2)


with open("data2.json", "w") as file:
    file.write(json_object)


# # ______------____----Delete Dictionary
# a = {1:10, 2:20, 3:30}
# a.pop(1)
# print(a)