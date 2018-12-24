import random
import os
import subprocess
import time

class playMusicClass:
	def play(self):
		r = random.randrange(1,10)
		string = str(r)+".mp3"
		print(string)
		self.music = subprocess.Popen(['rhythmbox',string],stdout = subprocess.PIPE)
		#os.system(string)
		return self.music
	def stop(self,m):
		m.kill()



