import pyttsx3
import os

pyttsx3.speak("Good Morning")
print("Good Morning")


#Python program using input function
a = input ("Enter ur name: ")
print ("Hi", a)
pyttsx3.speak("Hi")

print("Welcome to my tools")
pyttsx3.speak("Welcome to my tools")
pyttsx3.speak("How can I help u")

b = input ("How can I help u: ")
pyttsx3.speak("I can open notepad")
print("Notepad")
pyttsx3.speak("I can open chrome")
print("Chrome")
pyttsx3.speak("I can open Social media- like whatsapp")
print("Social media- whatsApp,")
pyttsx3.speak("linkedIn")
print("linkedIn,")
pyttsx3.speak("github")
print("github")
pyttsx3.speak("I can open gmail")
print("gmail")
pyttsx3.speak("I can open Games")
print("Games")
pyttsx3.speak("I can open calculator")
print("Calculator")


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

	elif (("r" in p) or ("are" in p) or ("Hey" in p))  and (("you" in p) or ("u" in p)) and ("alexa" in p):
	  pyttsx3.speak("I m not Alexa, but something like Alexa")

	elif (("run" in p) or ("start" in p) or ("open" in p)) and ("mail" in p):
	  pyttsx3.speak("mail is opening")
	  os.system("chrome www.gmail.com")

	elif (("run" in p) or ("start" in p) or ("open" in p)) and ("dictionary" in p):
	  pyttsx3.speak("open dictionary")
	  os.system("chrome https://translate.google.com/?rlz=1C1CHBF_enIN911IN911&um=1&ie=UTF-8&hl=en&client=tw-ob#en/hi/")

	elif ("aws" in p) or ("aws cloud services" in p):
	  os.system("chrome https://aws.amazon.com/") 
	  pyttsx3.speak("opening amazon web services")        

	elif (("run" in p) or ("start" in p) or ("open" in p)) and ("portal" in p):
	  os.system("chrome https://glauniversity.in:8085/")
	  pyttsx3.speak("portal is open")
      
	elif (("run" in p) or ("start" in p) or ("open" in p)) and ("linkedin" in p):
	  os.system("chrome www.linkedIn.com")
	  pyttsx3.speak("linkedIn is open")

	elif (("run" in p) or ("start" in p) or ("open" in p)) and ("github" in p):
	  os.system("chrome www.github.com")
	  pyttsx3.speak("github is open")

	elif (("run" in p) or ("start" in p) or ("open" in p)) and ("tenda" in p):
	  os.system("chrome http://192.168.0.1/login.html")
	  pyttsx3.speak("tenda is open")

	elif (("run" in p) or ("start" in p) or ("open" in p)) and ("whatsapp" in p):
	  pyttsx3.speak("whatsApp is opening")
	  os.system("chrome https://web.whatsapp.com/")

	elif ("Python" in p) or ("what is python" in p) or ("something about python" in p):
	  os.system("chrome www.python.org")
	  pyttsx3.speak("U can search anything about python here")

	elif (("run" in p) or ("start" in p) or ("open" in p)) and ("youtube" in p):
	  os.system("chrome www.youtube.com")
	  pyttsx3.speak("opening youtube")

	elif (("run" in p) or  ("execute" in p ) or ("open" in p) or ("start" in p)) and  (("notepad" in p) or ("editor" in p) ) :
	  pyttsx3.speak("notepad is opening")
	  os.system("notepad")

	elif (("run" in p) or ("play" in p) or ("start" in p) or ("open" in p))  and ("media" in p) and ("player" in p):
	  os.system("start wmplayer")
	  pyttsx3.speak("window media player is open successfully")

	elif (("open" in p) or ("start" in p))  and (("calc" in p) or ("calculator" in p)):
	  os.system("calc")
	  pyttsx3.speak("calculator is open")


	elif ("exit" in p)  or ("quit" in p) or ("stop" in p) or ("close" in p) or ("out" in p):
	  break

	else:
	  print("dont support")

print("Okay")
pyttsx3.speak("Okay!")
print("Thank you! Bye. Have a good day.")
pyttsx3.speak("Thank you! Bye. Have a good day.")
