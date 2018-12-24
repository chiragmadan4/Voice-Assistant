import speech_recognition as sr
import txttosp
r = sr.Recognizer()
def record():
	text = "none"
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source,duration = 2)
		print("recording audio");
		audio = r.listen(source)
		print("recorded")
		try:
			text = r.recognize_google(audio) 
			print("You said: "+text);
		except:
			#txttosp.convertToAudio("Cannot hear you. Could you please repeat?")
			print("exception in recording")
	if text is not "none":	
		return text
	else:
		return "none"


