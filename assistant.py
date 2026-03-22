import speech_recognition as sr
import pyttsx3
import os
import subprocess
import json
import webbrowser
import random

def greeting():

 responses=[
 "Yes Sir",
 "I'm listening Sir",
 "Ready Sir",
 "Ready to help Sir",
 "I am here to help you Sir"
 ]

 speak(random.choice(responses))

# ---------------- SPEAK ----------------

def speak(text):

 import pyttsx3

 print("Assistant:",text)

 engine=pyttsx3.init()
 engine.setProperty("rate",170)

 engine.say(text)
 engine.runAndWait()
 engine.stop()

# ---------------- SPEECH RECOGNITION ----------------

recognizer=sr.Recognizer()
recognizer.energy_threshold=300
recognizer.pause_threshold=1.2

memory_file="memory.json"

# ---------------- LISTEN ----------------

def listen():

 try:

  with sr.Microphone() as source:

   print("Listening...")

   recognizer.adjust_for_ambient_noise(source,duration=0.5)

   audio=recognizer.listen(source,timeout=5)

  command=recognizer.recognize_google(audio)

  print("You said:",command)

  return command.lower()

 except sr.WaitTimeoutError:

  return ""

 except sr.UnknownValueError:

  return ""

 except Exception as e:

  print("Listening error:",e)

  return ""
 
# ---------------- MEMORY ----------------

def load_memory():

 if not os.path.exists(memory_file):

  with open(memory_file,"w") as f:
   json.dump({},f)

  return {}

 with open(memory_file,"r") as f:
  return json.load(f)

def save_memory(data):

 with open(memory_file,"w") as f:
  json.dump(data,f,indent=4)

memory=load_memory()

def remember(command):

 if "remember" in command:

  info=command.replace("remember","").strip()

  memory[str(len(memory)+1)]=info

  save_memory(memory)

  speak("Okay Legend, I will remember that")

  return True

 return False

# ---------------- AI ----------------

def ai_response(prompt):

 context="\n".join(memory.values())

 result=subprocess.run(
  ["ollama","run","llama3",context+"\nUser:"+prompt],
  capture_output=True,
  text=True,
  encoding="utf-8",
  errors="ignore"
 )

 return result.stdout

# ------------ System Commands --------------

def system_commands(command):

 if "shutdown pc" in command:
  speak("Shutting down the system")
  os.system("shutdown /s /t 5")
  return True

 elif "restart pc" in command:
  speak("Restarting the system")
  os.system("shutdown /r /t 5")
  return True

 elif "lock pc" in command:
  speak("Locking the computer")
  os.system("rundll32.exe user32.dll,LockWorkStation")
  return True

 elif "sleep pc" in command:
  speak("Putting the computer to sleep")
  os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
  return True

 elif "task manager" in command:
  speak("Opening Task Manager")
  os.system("start taskmgr")
  return True

 elif "control panel" in command:
  speak("Opening Control Panel")
  os.system("start control")
  return True

 elif "settings" in command:
  speak("Opening Settings")
  os.system("start ms-settings:")
  return True

 return False

# ---------------- OPEN APPS ----------------

def open_apps(command):

 if "word" in command:
  speak("Opening Microsoft Word")
  os.system("start winword")
  return True

 elif "excel" in command:
  speak("Opening Microsoft Excel")
  os.system("start excel")
  return True

 elif "powerpoint" in command:
  speak("Opening PowerPoint")
  os.system("start powerpnt")
  return True

 elif "vs code" in command:
  speak("Opening VS Code")
  os.system("code")
  return True

 elif "notepad" in command:
  speak("Opening Notepad")
  os.system("start notepad")
  return True

 elif "chrome" in command:
  speak("Opening Chrome")
  os.system("start chrome")
  return True

 elif "file explorer" in command:
  speak("Opening File Explorer")
  os.system("explorer")
  return True
 
 elif "paint" in command:
  speak("Opening Paint")
  os.system("start mspaint")
  return True

 elif "calculator" in command:
  speak("Opening Calculator")
  os.system("start calc")
  return True

 elif "clock" in command:
  speak("Opening Clock")
  os.system("start ms-clock:")
  return True

 elif "microsoft store" in command:
  speak("Opening Microsoft Store")
  os.system("start ms-windows-store:")
  return True

 elif "obs" in command or "obs studio" in command:
  speak("Opening OBS Studio")
  os.system("start obs64")
  return True

 elif "pycharm" in command or "python ide" in command:
  speak("Opening PyCharm")
  os.system("start pycharm64")
  return True

 elif "logitech g hub" in command:
  speak("Opening Logitech G Hub")
  os.system("start lghub")
  return True
 
 elif "alienware command center" in command:
  speak("Opening Alienware Command Center")
  os.system(r"C:\Program Files\Alienware\Alienware Command Center\AWCC\AWCC.exe")
  return True

 elif "feather" in command or "feather client" in command or "feather launcher" in command:
  speak("Opening Feather Client")
  os.startfile(r"C:\Program Files\Feather Launcher\Feather Launcher.exe")
  return True

 elif "lunar" in command or "lunar client" in command or "lunar launcher" in command:
  speak("Opening Lunar Client")
  os.startfile(r"C:\Users\Mohd Saad\AppData\Local\Programs\Lunar Client\Lunar Client.exe")
  return True

 elif "modrinth" in command:
  speak("Opening Modrinth")
  os.startfile(r"C:\Users\Mohd Saad\AppData\Local\Modrinth App\Modrinth App.exe")
  return True

 elif "curseforge" in command:
  speak("Opening CurseForge")
  os.startfile(r"C:\Program Files (x86)\Overwolf\Overwolf.exe")
  return True

 elif "sk launcher" in command or "sklauncher" in command:
  speak("Opening SKLauncher")
  os.startfile(r"C:\Users\Mohd Saad\AppData\Roaming\sklauncher\jre\bin\javaw.exe")
  return True

 elif "minecraft launcher" in command or "minecraft" in command:
  speak("Opening Minecraft Launcher")
  os.startfile(r"C:\XboxGames\Minecraft Launcher\Content\Minecraft.exe")
  return True

 elif "asphalt" in command or "asphalt legends" in command:
  speak("Opening Asphalt Legends")
  os.startfile(r"C:\XboxGames\Asphalt Legends Unite\Content\Asphalt9_gdk_x64_rtl.exe")
  return True
 
 elif "discord" in command:
  speak("Opening Discord")
  os.startfile(r"C:\Users\Mohd Saad\AppData\Local\Discord\app-1.0.9226\Discord.exe")
  return True
 
 elif "canva" in command:
  speak("Opening Canva Application")
  os.startfile(r"C:\Users\Mohd Saad\AppData\Local\Programs\Canva\Canva.exe")
  return True
 
 elif "lets play" in command or "game on" in command:
  speak("Ok Legend! Opening Discord and Feather Client! And closing all other Applications!")
  close_apps("close everything")
  os.startfile(r"C:\Program Files\Feather Launcher\Feather Launcher.exe")
  os.startfile(r"C:\Users\Mohd Saad\AppData\Local\Discord\app-1.0.9226\Discord.exe")
  return True

 elif "activate python mode" in command:
  speak("Done Legend! Python mode Activated. Closing other applications")
  close_apps("close everything")
  os.system("start pycharm64")
  os.startfile(r"C:\Users\Mohd Saad\OneDrive\Desktop\4. Vidyalankar Polytechnic CO4KA\PWP")
  os.system("start chrome https://chatgpt.com/")
  os.system("start chrome https://web.whatsapp.com/")
  return True
 
 elif "activate java mode" in command:
  speak("Done Legend! Java mode Activated. Closing other applications")
  close_apps("close everything")
  os.system("start notepad")
  os.startfile(r"C:\Users\Mohd Saad\OneDrive\Desktop\4. Vidyalankar Polytechnic CO4KA\JPR")
  os.system("start chrome https://chatgpt.com/")
  os.system("start chrome https://web.whatsapp.com/")
  return True
 
 elif "activate ui mode" in command or "activate ui mod" in command or "activate gui mode" in command:
  speak("Done Legend! UI UX mode Activated. Closing other applications")
  close_apps("close everything")
  os.startfile(r"C:\Users\Mohd Saad\OneDrive\Desktop\4. Vidyalankar Polytechnic CO4KA\UID")
  open_websites("figma")
  os.system("start chrome https://chatgpt.com/")
  os.system("start chrome https://web.whatsapp.com/")
  return True

 return False

# ---------------- OPEN WEBSITES ----------------

def open_websites(command):

 if "youtube" in command:
  speak("Opening YouTube")
  webbrowser.open("https://youtube.com")
  return True

 elif "chat gpt" in command:
  speak("Opening ChatGPT")
  os.system("start chrome https://chatgpt.com/")
  return True

 elif "whatsapp" in command:
  speak("Opening WhatsApp Web")
  os.system("start chrome https://web.whatsapp.com/")
  return True

 elif "canva web" in command:
  speak("Opening Canva")
  os.system("start chrome https://www.canva.com/")
  return True
 
 elif "figma" in command:
  speak("Opening Figma")
  os.system("start chrome https://www.figma.com/files/team/1582260448694216831/recents-and-sharing?fuid=1582260444230613719/")
  return True
 return False

# ---------------- AUTO OPEN SOFTWARE ----------------

def open_any_app(command):

 if command.startswith("open "):

  app_name=command.replace("open","").strip()

  try:

   speak("Opening "+app_name)

   os.system('start "" '+app_name)

   return True

  except:

   return False

 return False

# ---------------- CLOSE APPS ----------------

def close_apps(command):

 if "close chrome" in command or "closed chrome" in command:
  speak("Closing Chrome")
  os.system("taskkill /im chrome.exe /f")
  return True

 elif "close word" in command or "closed word" in command:
  speak("Closing Word")
  os.system("taskkill /im winword.exe /f")
  return True

 elif "close excel" in command or "closed excel" in command:
  speak("Closing Excel")
  os.system("taskkill /im excel.exe /f")
  return True

 elif "close powerpoint" in command or "closed powerpoint" in command:
  speak("Closing PowerPoint")
  os.system("taskkill /im powerpnt.exe /f")
  return True

 elif "close vscode" in command or "close vs code" in command  or "closed vs code" in command:
  speak("Closing VS Code")
  os.system("taskkill /im Code.exe /f")
  return True

 elif "close notepad" in command or "closed notepad" in command:
  speak("Closing Notepad")
  os.system("taskkill /im notepad.exe /f")
  return True

 elif "close youtube" in command or "closed youtube" in command:
  speak("Closing browser")
  os.system("taskkill /im chrome.exe /f")
  return True

 elif "close edge" in command or "closed edge" in command:
  speak("Closing Microsoft Edge")
  os.system("taskkill /im msedge.exe /f")
  return True
 
 elif "close paint" in command or "closed paint" in command:
  speak("Closing Paint")
  os.system("taskkill /im mspaint.exe /f")
  return True
 
 elif "close calculator" in command or "closed calculator" in command:
  speak("Closing Calculator")
  os.system("taskkill /im calc.exe /f")
  return True

 elif "close clock" in command or "closed clock" in command:
  speak("Closing Clock")
  os.system("taskkill /im ClockApp.exe /f")
  return True

 elif "close microsoft store" in command or "closed microsoft store" in command:
  speak("Closing Microsoft Store")
  os.system("taskkill /im WinStore.App.exe /f")
  return True

 elif "close obs" in command or "close obs studio" in command or "closed obs" in command or "closed obs studio" in command:
  speak("Closing OBS Studio")
  os.system("taskkill /im obs64.exe /f")
  return True

 elif "close pycharm" in command or "closed pycharm" in command:
  speak("Closing PyCharm")
  os.system("taskkill /im pycharm64.exe /f")
  return True

 elif "close feather client" in command or "close feather" in command or "closed feather" in command or "closed feather client" in command:
  speak("Closing Feather Client")
  os.system("taskkill /im Feather Launcher.exe /f")
  return True

 elif "close lunar client" in command or "close lunar" in command or "closed lunar client" in command or "close lunar" in command:
  speak("Closing Lunar Client")
  os.system("taskkill /im Lunar Client.exe /f")
  return True

 elif "close modrinth" in command or "closed modrinth" in command:
  speak("Closing Modrinth")
  os.system("taskkill /im Modrinth App.exe /f")
  return True

 elif "close curseforge" in command or "closed curseforge" in command:
  speak("Closing CurseForge")
  os.system("taskkill /im Overwolf.exe /f")
  return True

 elif "close sk launcher" in command or "closed sk launcher" in command:
  speak("Closing SKLauncher")
  os.system("taskkill /im javaw.exe /f")
  return True

 elif "close minecraft" in command or "close minecraft launcher" in command or "closed minecraft" in command or "closed minecraft launcher" in command:
  speak("Closing Minecraft")
  os.system("taskkill /im Minecraft.exe /f")
  return True

 elif "close asphalt" in command or "close asphalt legends" in command or "closed asphalt" in command or "closed asphalt legends" in command:
  speak("Closing Asphalt Legends")
  os.system("taskkill /im Asphalt9_gdk_x64_rtl.exe /f")
  return True
 
 elif "close discord" in command or "closed discord" in command:
  speak("Closing Discord")
  os.system("taskkill /im discord.exe /f")
  return True

 elif "close canva" in command or "closed canva" in command:
  speak("Closing Canva Application")
  os.system("taskkill /im canva.exe /f")
  return True

 elif "close all tabs" in command or "close everything" in command or "closes all tabs" in command or "closes everything" in command:

  speak("Closing all applications")

  os.system("taskkill /im chrome.exe /f")
  os.system("taskkill /im msedge.exe /f")
  os.system("taskkill /im winword.exe /f")
  os.system("taskkill /im excel.exe /f")
  os.system("taskkill /im powerpnt.exe /f")
  os.system("taskkill /im Code.exe /f")
  os.system("taskkill /im notepad.exe /f")
  os.system("taskkill /im mspaint.exe /f")
  os.system("taskkill /im calc.exe /f")
  os.system("taskkill /im ClockApp.exe /f")
  os.system("taskkill /im WinStore.App.exe /f")
  os.system("taskkill /im obs64.exe /f")
  os.system("taskkill /im pycharm64.exe /f")
  os.system("taskkill /im Feather Launcher.exe /f")
  os.system("taskkill /im Lunar Client.exe /f")
  os.system("taskkill /im Modrinth App.exe /f")
  os.system("taskkill /im Overwolf.exe /f")
  os.system("taskkill /im javaw.exe /f")
  os.system("taskkill /im Minecraft.exe /f")
  os.system("taskkill /im Asphalt9_gdk_x64_rtl.exe /f")
  os.system("taskkill /im discord.exe /f")
  os.system("taskkill /im canva.exe /f")

  return True

 elif "close all games" in command or "closed all games" in command:
  speak("Ok Legend! Closing all the Games")
  os.system("taskkill /im Feather Launcher.exe /f")
  os.system("taskkill /im Lunar Client.exe /f")
  os.system("taskkill /im Modrinth App.exe /f")
  os.system("taskkill /im Overwolf.exe /f")
  os.system("taskkill /im javaw.exe /f")
  os.system("taskkill /im Minecraft.exe /f")
  os.system("taskkill /im Asphalt9_gdk_x64_rtl.exe /f")
  os.system("taskkill /im discord.exe /f")
  return True

 return False

# ---------------- INTERNET SEARCH ----------------

def internet_search(command):

 if "search youtube for" in command:
  query=command.replace("search youtube for","").strip()
  speak("Searching YouTube")
  webbrowser.open("https://www.youtube.com/results?search_query="+query)
  return True


 elif "search wikipedia for" in command:
  query=command.replace("search wikipedia for","").strip()
  speak("Searching Wikipedia")
  webbrowser.open("https://en.wikipedia.org/wiki/"+query)
  return True


 elif "search for" in command or "google" in command:
  query=command.replace("search for","").replace("google","").strip()
  speak("Searching the internet")
  webbrowser.open("https://www.google.com/search?q="+query)
  return True

 return False

# ---------------- MAIN LOOP ----------------

print("G15 Assistant Ready")

wake_words=[
"hey g15",
"cg 15",
"pg 15",
"pc 15",
"80 15",
"8015",
"age 15",
"ac 15",
"ag 15",
"g15",
"g 15",
"lazy 15",
"ali 15",
"lg 15",
"music 15",
"v15",
"v 15",
"t 15",
"t15",
"c 15",
"c15",
"chal bhai",
"chalbhai",
"play 15",
"jarvis",
"hey jarvis"
]

while True:

 command=listen()

 if any(word in command for word in wake_words):

  greeting()

  for word in wake_words:
   command=command.replace(word,"")

  command=command.strip()

  if command=="":
   command=listen()

   if command=="":
    continue

   if remember(command):
    continue

  if close_apps(command):
   continue

  if open_apps(command):
   continue

  if open_websites(command):
   continue

  if system_commands(command):
   continue

  if open_any_app(command):
   continue

  if internet_search(command):
   continue

  speak("Hang on Legend, thinking about it...")

  answer=ai_response(command)

  print(answer)

  speak(answer)