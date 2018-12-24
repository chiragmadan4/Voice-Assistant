import start
import txttosp
import getWeather
import time
import playMusic
import re
from datetime import date
import calendar
import nltk
import speechToText
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
notStopwords = ['what','do','who']



def getTasks():
	for i in range(len(tasks)):
		if tasks[i].status == "incomplete":
			taskAudioString = tasks[i].task+" "+"at"+" "+tasks[i].time
			txttosp.convertToAudio(taskAudioString)

class ToDo:
	def __init__(self,task,time,status = "incomplete"):
		self.task = task
		self.time = time
		self.status = status


tasks = []
#start.tellAboutTheDay()
string = raw_input("input\n")

'''string = speechToText.record()
while string == "none":
	time.sleep(1)
	string = speechToText.record()'''
 
playMusicObj = playMusic.playMusicClass()
returnedMusicObject = None
while 0<1:
	processedString = re.sub('[^a-zA-Z0-9]', ' ', string)
	processedString.lower()
	list = processedString.split()
	ps  = PorterStemmer()
	processedList = []
	processedList = [word for word in list if not word in set(stopwords.words('english')).difference(notStopwords)]
	print("processedList",processedList)
	if "songs" in processedList or "song" in processedList or "music" in processedList:
		if "play" in processedList or "change" in processedList:
			returnedMusicObject = playMusicObj.play()
		elif "stop" in processedList or "pause" in processedList:
			if returnedMusicObject is not None:
				playMusicObj.stop(returnedMusicObject)
				returnedMusicObject = None
				print("music kill attempt made")
			else:
				txttosp.convertToAudio("No songs are playing.")
	elif "tasks" in processedList or "task" in processedList:
		if "add" in processedList or "write" in processedList or "note" in processedList or "down" in processedList or "make" in processedList or "entry" in processedList:
			txttosp.convertToAudio("what task you want to do?")
			'''task = speechToText.record()
			while task == "none":
				task = speechToText.record()'''
			task = raw_input("what task you want to do?\n")
			txttosp.convertToAudio("At what time you want to do your task?")
			'''taskTime = speechToText.record()
			while taskTime == "none":
				taskTime = speechToText.record()'''

			taskTime = raw_input("At what time you want to do your task?\n")
			taskObj = ToDo(task,taskTime)
			tasks.append(taskObj)
			txttosp.convertToAudio("Task was successfully added to your to-do list.")
		elif "tell" in processedList or "what" in processedList:
			if len(tasks) == 0:
				txttosp.convertToAudio("You have no tasks in your to-do list.")
			else:
				txttosp.convertToAudio("You have the following tasks to do:")
				getTasks()
		elif "remove" in processedList or "complete" in processedList or "mark" in processedList or "done" in processedList or "delete" in processedList:
			txttosp.convertToAudio("Which task you want to mark completed?")
		else:
			print("invalid task operation")
	elif "bye" in processedList or "goodbye" in processedList or "shut" in processedList:
		txttosp.convertToAudio("It was nice assisting you")
		txttosp.convertToAudio("Have a nice day!")
		break
	elif "can" in processedList or "do" in processedList:
		txttosp.convertToAudio("Sorry, currently I do not have this functionality.\n")
	elif "made" in processedList or "created" in processedList or "who" in processedList:
		start.creator()
	elif "introduce" in processedList:
		start.introduce()
	elif "temperature" in processedList and "what" in processedList:
		txttosp.convertToAudio(getWeather.temperature())
	else:
		txttosp.convertToAudio("I didn't get you, could you please repeat.")
		print("invalid")
	string = raw_input("input\n")
	'''string = speechToText.record() 
	while string == "none":
		time.sleep(1)
		string = speechToText.record()'''

