from datetime import date
import calendar
import txttosp
import getWeather

def tellAboutTheDay():
	my_date = date.today()
	greetString = "Today is "+str(my_date)+", "+calendar.day_name[my_date.weekday()]+". "+str(getWeather.getWeather())
	txttosp.convertToAudio(greetString)
	txttosp.convertToAudio("How can I help you?")	
def creator():
	string = "I was created by Chirag."
	txttosp.convertToAudio(string)
def introduce():
	string = "My name is Victoria. I am your personal voice assistant."
	txttosp.convertToAudio(string)
