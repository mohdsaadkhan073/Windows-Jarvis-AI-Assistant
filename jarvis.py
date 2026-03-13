import speech_recognition as sr
import pyttsx3
import os
import subprocess
import json
import webbrowser
import random
import pyautogui 
import pytesseract 
import keyboard
import time
import re

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

engine=pyttsx3.init()
engine.setProperty("rate",170)

stop_speaking=False

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

 global stop_speaking

 print("Assistant:",text)

 stop_speaking=False

 engine.say(text)
 engine.startLoop(False)

 while engine.isBusy():

  engine.iterate()

  if stop_speaking:
   engine.stop()
   break

 engine.endLoop()

def stop_speech():

 global stop_speaking
 stop_speaking=True

keyboard.add_hotkey("ctrl+shift",stop_speech)





# ---------------- SPEECH RECOGNITION ----------------

recognizer=sr.Recognizer()
recognizer.energy_threshold=300
recognizer.pause_threshold=2.2
recognizer.dynamic_energy_threshold=True

memory_file="memory.json"





# ---------------- LISTEN ----------------

def listen():

 try:

  with sr.Microphone() as source:

   print("Listening...")

   recognizer.adjust_for_ambient_noise(source,duration=1)

   audio=recognizer.listen(source, phrase_time_limit=30)

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

  speak("Okay Sir, I will remember that")

  return True

 return False






# ---------------- AI ----------------

def ai_response(prompt):

 context="\n".join(memory.values())

 result=subprocess.run(
  ["ollama","run","deepseek-r1:7b",context+"\nUser:"+prompt],
  capture_output=True,
  text=True,
  encoding="utf-8",
  errors="ignore"
 )

 response=result.stdout

 if "</think>" in response:
  response=response.split("</think>")[-1]

 return response.strip()





# ------------ System Commands --------------

def system_commands(command):

 if "shutdown pc" in command or "shut down pc" in command:
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

 if "word" in command or "world" in command:
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

 elif "vs code" in command or "vs" in command:
  speak("Opening VS Code")
  os.system("code")
  return True

 elif "notepad" in command:
  speak("Opening Notepad")
  os.system("start notepad")
  return True

 elif "chrome" in command or "karo" in command:
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

 elif "calculator" in command or "calc" in command or "cal c" in command:
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
 
 elif "microsoft 365" in command or "ms 365" in command:
  speak("Opening Microsoft 365 Copilot")
  os.system("start explorer.exe shell:AppsFolder\Microsoft.MicrosoftOfficeHub_8wekyb3d8bbwe!Microsoft.MicrosoftOfficeHub")
  return True
 
 elif "ms teams" in command or "microsoft teams" in command or "teams" in command:
  speak("Opening Microsoft Teams")
  os.system("start ms-teams:")
  return True

 elif "obs" in command or "obs studio" in command:
  speak("Opening OBS Studio")
  os.system("start obs64")
  return True

 elif "pycharm" in command or "python ide" in command:
  speak("Opening PyCharm")
  os.system("start pycharm64")
  return True

 elif "logitech g hub" in command or "logitech" in command:
  speak("Opening Logitech G Hub")
  os.startfile(r"C:\Program Files\LGHUB\lghub.exe")
  return True
 
 elif "alienware command center" in command or "alienware" in command:
  speak("Opening Alienware Command Center")
  os.startfile(r"C:\Program Files\Alienware\Alienware Command Center\AWCC\AWCC.exe")
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
 
 elif "canva" in command:
  speak("Opening Canva Application")
  os.startfile(r"C:\Users\Mohd Saad\AppData\Local\Programs\Canva\Canva.exe")
  return True
 
 elif "lets play" in command or "game on" in command or "gaming on" in command or "activate gaming mode" in command or "activate gaming mod" in command:
  speak("Ok Legend! Opening Discord and Feather Client! And closing all other Applications!")
  close_apps("close everything")
  os.startfile(r"C:\Program Files\Feather Launcher\Feather Launcher.exe")
  os.startfile(r"C:\Users\Mohd Saad\AppData\Local\Discord\app-1.0.9226\Discord.exe")
  return True

 elif "activate python mode" in command or "activate python mod" in command or "activate python" in command or "python mode" in command or "python mod" in command:
  speak("Done Sir! Python mode Activated. Closing other applications")
  close_apps("close everything")
  os.system("start pycharm64")
  os.startfile(r"C:\Users\Mohd Saad\OneDrive\Desktop\4. Vidyalankar Polytechnic CO4KA\PWP")
  os.system("start chrome https://chatgpt.com/")
  os.system("start chrome https://web.whatsapp.com/")
  return True
 
 elif "activate java mode" in command or "activate java mod" in command or "activate java" in command or "java mode" in command or "java mod" in command:
  speak("Done Sir! Java mode Activated. Closing other applications")
  close_apps("close everything")
  os.system("start notepad")
  os.startfile(r"C:\Users\Mohd Saad\OneDrive\Desktop\4. Vidyalankar Polytechnic CO4KA\JPR")
  os.system("start chrome https://chatgpt.com/")
  os.system("start chrome https://web.whatsapp.com/")
  wt_path=r"C:\Users\Mohd Saad\AppData\Local\Microsoft\WindowsApps\wt.exe"
  java_path=r"C:\Users\Mohd Saad\OneDrive\Desktop\4. Vidyalankar Polytechnic CO4KA\JPR\My Practice"
  subprocess.Popen([wt_path,"-w","0","nt","-d",java_path,"cmd"])
  return True
 
 elif "activate ui mode" in command or "activate ui mod" in command or "activate gui mode" in command or "activate gui mod" in command or "activate ui" in command or "ui mode" in command or "ui mod" in command or "gui mode" in command or "gui mod" in command:
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

def extract_app_name(command):
 cmd=command.lower().strip()

 # patterns like:
 # open telegram
 # start telegram
 # launch telegram
 m=re.search(r'^(open|start|launch)\s+(.+)$',cmd)
 if m:
  return m.group(2).strip()

 # patterns like:
 # telegram open
 # telegram start
 # telegram launch
 m=re.search(r'^(.+?)\s+(open|start|launch)$',cmd)
 if m:
  return m.group(1).strip()

 # patterns like:
 # please open telegram
 m=re.search(r'^(please\s+)?(open|start|launch)\s+(.+)$',cmd)
 if m:
  return m.group(3).strip()

 return None

def open_any_app(command):
 app_name=extract_app_name(command)
 if not app_name:
  return False

 speak("Opening "+app_name)

 try:
  # pyautogui.hotkey('win','d')
  time.sleep(0.4)
  pyautogui.press('win')
  time.sleep(1)
  pyautogui.write(app_name,interval=0.02)
  time.sleep(1)
  pyautogui.press('enter')
  return True
 except:
  return False







# ----------------------------------- Search Folders/Files ----------------------------------

# -------- VOICE NUMBER PARSER --------
def get_voice_number():
 text=listen()
 if not text:
  return None

 text=text.lower()

 # direct digit (e.g., "2", "option 3")
 import re
 m=re.search(r'\d+',text)
 if m:
  return int(m.group())

 word_map={
  "one":1,"two":2,"three":3,"four":4,"five":5,
  "six":6,"seven":7,"eight":8,"nine":9,"ten":10,
  "first":1,"second":2,"third":3,"fourth":4,"fifth":5,
  "sixth":6,"seventh":7,"eighth":8,"ninth":9,"tenth":10
 }

 for word,num in word_map.items():
  if word in text:
   return num

 return None

# -------- COMMAND PARSER --------
def parse_command(command):
 cmd=command.lower().strip()

 patterns=[
  ("open folder ","folder","open"),
  ("search folder ","folder","search"),
  ("open file ","file","open"),
  ("search file ","file","search")
 ]

 for prefix,stype,act in patterns:
  if cmd.startswith(prefix):
   name=cmd.replace(prefix,"",1).strip()
   return name,stype,act

 return None,None,None

# -------- MAIN FUNCTION --------
def handle_file_folder_command(command):
 name,search_type,action=parse_command(command)
 if not name:
  return False

 speak(f"{action}ing {search_type} {name}")

 import subprocess,os

 # -------- FAST SEARCH --------
 if search_type=="file":
  cmd=f'where /r C:\\ "{name}.*"'
  results=subprocess.getoutput(cmd).splitlines()
 else:
  ps_cmd=(
   'powershell -command '
   '"Get-ChildItem -Path C:\\ -Directory -Filter '
   f'\'{name}\' -Recurse -ErrorAction SilentlyContinue | '
   'Select-Object -ExpandProperty FullName"'
  )
  results=subprocess.getoutput(ps_cmd).splitlines()

 results=[r.strip() for r in results if r.strip()]

 # -------- NO RESULT --------
 if not results:
  speak(f"{search_type} not found")
  return True

 # -------- SEARCH MODE --------
 if action=="search":
  if len(results)==1:
   speak("One result found. Opening it.")
   os.startfile(results[0])
   return True

  speak(f"I found {len(results)} results")
  for i,p in enumerate(results[:5]):
   print(f"{i+1}. {p}")

  speak("Say the number to open")
  choice=get_voice_number()

  if choice and 1<=choice<=len(results[:5]):
   os.startfile(results[choice-1])
   speak("Opening selected one")
  else:
   speak("Invalid choice")

  return True

 # -------- OPEN MODE --------
 if len(results)==1:
  os.startfile(results[0])
  speak("Opening now")
  return True

 speak(f"I found {len(results)} {search_type}s")
 speak("Here are top results")

 for i,p in enumerate(results[:5]):
  print(f"{i+1}. {p}")

 speak("Say the number to open")
 choice=get_voice_number()

 if choice and 1<=choice<=len(results[:5]):
  os.startfile(results[choice-1])
  speak("Opening selected one")
 else:
  speak("Invalid choice")

 return True






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






# ------------------- Screen Read OCR ---------------------

def read_screen():

 speak("Reading the screen")

 screenshot=pyautogui.screenshot()

 screenshot.save("screen.png")

 text=pytesseract.image_to_string(screenshot)

 if text.strip()=="":
  speak("I could not detect any text on the screen")
  return ""

 print("Screen Text:\n",text)

 return text

def read_selected_area():

 speak("Move mouse to top left corner and press control")

 keyboard.wait("ctrl")

 x1,y1=pyautogui.position()

 speak("Now move mouse to bottom right corner and press control")

 keyboard.wait("ctrl")

 x2,y2=pyautogui.position()

 width=x2-x1
 height=y2-y1

 screenshot=pyautogui.screenshot(region=(x1,y1,width,height))

 text=pytesseract.image_to_string(screenshot)

 if text.strip()=="":
  speak("No text detected in selected area")
  return ""

 print("Selected Area Text:\n",text)

 return text






# --------------- Screen Analysis of OCR -----------------

def analyze_screen(command):

 text=read_screen()

 if text=="":
  return True

 speak("Analyzing what is on the screen")

 answer=ai_response("User request:\n"+command+"\n\nScreen content:\n"+text)

 print(answer)

 speak(answer)

 return True

def analyze_selected_area(command):

 text=read_selected_area()

 if text=="":
  return True

 speak("Analyzing selected area")

 answer=ai_response("User request:\n"+command+"\n\nScreen content:\n"+text)

 print(answer)

 speak(answer)

 return True






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
"aj 15",
"g15",
"g 15",
"lazy 15",
"ali 15",
"lg 15",
"e15",
"e 15"
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
"hey jarvis",
"heyjarvis",
"hi jarvis",
"hijarvis",
"is jarvis",
"which jarvis",
"jarvis",
"dell g15",
"dell 15",
"dellg15",
"dellg",
"315"
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

  if internet_search(command):
   continue

  if handle_file_folder_command(command):
   continue

  if open_apps(command):
   continue

  if open_websites(command):
   continue

  if system_commands(command):
   continue

  if open_any_app(command):
   continue


  if "selected area" in command or "selected screen" in command:
   analyze_selected_area(command)
   continue

  if "analyze screen" in command or "read screen" in command or "what is on screen" in command or "analyse screen" in command or "analyse the screen" in command or "analyze the screen" in command:
   analyze_screen(command)
   continue


  speak("Hang on Sir, thinking about it...")

  answer=ai_response(command)

  speak(answer)
