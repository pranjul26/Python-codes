import pyttsx3
import os

# pyttsx3.speak("Welcome to my tools")

print()
print("Press 1: to open chrome")
print("Press 2: to open notepad")
print("Press 3: to open media player")
print()

print("enter your choice: " , end='')
p=input()
# print(p)
# os.system(p)


if int(p) == 1:
  os.system("chrome")
elif int(p) == 2:
  os.system("notepad")
elif int(p) == 3:
  os.system("start wmplayer")
else:
  print("don't supported")
