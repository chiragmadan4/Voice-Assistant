import urllib,json

url="http://api.openweathermap.org/data/2.5/forecast?id=1260107&appid=27380ef318b3d3478eca735fc8837e71"
response = urllib.urlopen(url)
data = json.loads(response.read())
print (type(data))
print(round(data["list"][0]["main"]["temp"]-273,2))
#print(data["list"])
