import pyttsx3
import os

print("Welcome to my tools")
pyttsx3.speak("Welcome to my tools")

while True:
	pyttsx3.speak("Tell me what are your requirements")
	print("Tell me what are your requirements : "  , end='')
	p = input()

	# print(p)
	# os.system(p)

	if (("run" in p) or ("start" in p) or ("open" in p))  and ("chrome" in p):
	  os.system("start chrome")
	  pyttsx3.speak("chrome is open successfully")

	elif (("run" in p) or  ("execute" in p ) or ("open" in p) or ("start" in p)) and  (("notepad" in p) or ("editor" in p) ) :
	  os.system("notepad")
	  pyttsx3.speak("notepad is open successfully")

	elif (("run" in p) or ("play" in p) or ("start" in p) or ("open" in p))  and ("media" in p) and ("player" in p):
	  os.system("start wmplayer")
	  pyttsx3.speak("window media player is open successfully")

	elif ("open" in p) or ("start" in p))  and (("calc" in p) or ("calculator" in p)):
	  os.system("calc")
	  pyttsx3.speak("calculator is open successfully")

	elif ("open" in p)  and ("edge" in p):
	  os.system("Microsoft Edge")
	  pyttsx3.speak("Microsoft edge is open successfully")

	elif  ("exit" in p)  or ("quit" in p) or ("stop" in p) or ("close" in p) or ("out" in p):
	  break

	else:
	  print("dont support")

print("Thank you! Have a good day!")
pyttsx3.speak("Thank you! Have a good day!")
