import requests

BASE = "http://localhost:5000/"

data = [
    {"likes": 200, "name": "Joe", "views": 10000},
    {"likes": 150, "name": "Howto", "views": 17000},
    {"likes": 2000, "name": "Trtr", "views": 26000}
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())
