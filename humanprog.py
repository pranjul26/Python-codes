import pyttsx3
import os

pyttsx3.speak("Good Morning")
print("Good Morning")

pyttsx3.speak("What is ur name:")
name = input('What is ur name:\n')
print ('Hi, %s.' % name)
pyttsx3.speak("Hi")

print("Welcome to my tools")
pyttsx3.speak("Welcome to my tools")
pyttsx3.speak("How can I help u")
print("How can I help u : " , end='')

print("please open files for me")
pyttsx3.speak("okay!")


while True:
	pyttsx3.speak("Tell me which file do you want to open")
	print("Tell me which file do you want to open : "  , end='')
	p = input()

	# print(p)
	# os.system(p) 

	if (("run" in p) or ("start" in p) or ("open" in p))  and ("chrome" in p):
	  os.system("start chrome")
	  pyttsx3.speak("okay! chrome is open successfully")

	elif (("run" in p) or  ("execute" in p ) or ("open" in p) or ("start" in p)) and  (("notepad" in p) or ("editor" in p) ) :
	  os.system("notepad")
	  pyttsx3.speak("notepad is open successfully")

	elif (("run" in p) or ("play" in p) or ("start" in p) or ("open" in p))  and ("media" in p) and ("player" in p):
	  os.system("start wmplayer")
	  pyttsx3.speak("window media player is open successfully")

	elif (("open" in p) or ("start" in p))  and (("calc" in p) or ("calculator" in p)):
	  os.system("calc")
	  pyttsx3.speak("calculator is open")

	elif ("open" in p)  and ("microsoft" in p):
	  os.system("start Microsoft")
	  pyttsx3.speak("microsoft is open successfully")
	

	elif ("exit" in p)  or ("quit" in p) or ("stop" in p) or ("close" in p) or ("out" in p):
	  break

	else:
	  print("dont support")

print("Okay")
pyttsx3.speak("Okay!")
print("Thank you! Bye. Have a good day.")
pyttsx3.speak("Thank you! Bye. Have a good day.")
