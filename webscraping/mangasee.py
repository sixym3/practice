import requests
import json

url = "https://mangasee123.com/read-online/Blue-Lock-chapter-189-page-1.html"
string_to_find = "function MainFunction($http, $timeout)"

response = requests.get(url).text
filtered_response = response[int(response.find(string_to_find)):]
filtered_response = filtered_response[int(filtered_response.find("vm.CHAPTERS")):int(filtered_response.find("vm.IndexName"))]
filtered_response = filtered_response[int(filtered_response.find("[")):int(filtered_response.find("]"))+1]
json_object = json.loads(filtered_response)
with open('webscraping/result.txt', "w") as result:
    result.write(filtered_response)
print(json_object[0]["Chapter"])