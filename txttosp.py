from gtts import gTTS 
import os 
from mutagen.mp3 import MP3
import time
import subprocess 
def convertToAudio(text):
	mytext = str(text)
	language = 'en'
	myobj = gTTS(text=mytext, lang=language, slow=False) 
	myobj.save("welcome.mp3") 
	audio = MP3("welcome.mp3")
	subprocess.Popen(['mpg321' ,'welcome.mp3'],stdout = subprocess.PIPE) 
	time.sleep(audio.info.length)

