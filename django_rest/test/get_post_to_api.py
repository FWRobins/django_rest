import requests

# get data
url = 'http://127.0.0.1:8000/api/heroes/'
headers = {'Authorization': 'Token 53ff163dbf80ab6be7091af095cb0c1656dad281'}
x = requests.get(url, headers = headers)
print(x.json())

# add data
# myobj = {'name':'Ironman',
#         'alias':'Tony Stark'}
#
# x = requests.post(url, data=myobj)
# print(x.json())
# print(x.text)

# get api auth Token
# url = 'http://127.0.0.1:8000/api-token-auth/'
# credentials = {'username':'admin1', 'password':'admin1'}
# x = requests.post(url, data = credentials)
# print(x.json())
