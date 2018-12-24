import urllib,json

def getWeather():
	url="http://api.openweathermap.org/data/2.5/forecast?id=1255744&appid=27380ef318b3d3478eca735fc8837e71"
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	#print (type(data))
	return "Current temperature is "+str((round(data["list"][0]["main"]["temp"]-273,2)))+" degree celcius"+" with "+data["list"][0]["weather"][0]['description']+"."

def temperature():
	url="http://api.openweathermap.org/data/2.5/forecast?id=1255744&appid=27380ef318b3d3478eca735fc8837e71"
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	return "Current temperature is "+str((round(data["list"][0]["main"]["temp"]-273,2)))+" degree celcius"+" with "+data["list"][0]["weather"][0]['description']+"."

# sonipat = 1255744
# patiala = 1260107
