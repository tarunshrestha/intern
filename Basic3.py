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
# # To add in new dictionary
# for i in data:
#     for j in countries:
#         if j == i['country']:
#             newDict.setdefault(j, []).append(i)
            
# # To remove country from new dict
# for i in newDict:
#     for j in newDict[i]:
#             j.pop('country')

# print(newDict)

# # # ______------____----Delete Dictionary
# # a = {1:10, 2:20, 3:30}
# # a.pop(1)
# # print(a)

# myLis = [1, 2, 3, 45, 6]
# print(id(myLis))
# a = myLis
# b = myLis.copy()

# print(id(a))
# print(id(b))

# # del a[1]
# # del b[1]

# print(myLis)
# print(a)
# print(b)

# print(myLis == a)
# print(myLis == b)
# print(myLis is a)
# print(myLis is b)

def tryi():
    for i in range(0, 5):
        yield i
    
print(next(tryi()))

for i in tryi():
    print(i)
