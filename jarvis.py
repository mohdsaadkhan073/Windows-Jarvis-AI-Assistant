import speech_recognition as sr
import pyttsx3
import subprocess
import threading
import keyboard
import time


stop_flag = False

engine = pyttsx3.init()
engine.setProperty("rate", 170)


def speak_chunk(text):
    global stop_flag
    if stop_flag:
        return
    engine.say(text)
    engine.runAndWait()


def speak(text):
    speak_chunk(text)


def extract_app_name(command):
    command = command.lower().strip()
    starters = ("please open ", "please start ", "please launch ", "open ", "start ", "launch ")
    endings = (" open", " start", " launch")

    for starter in starters:
        if command.startswith(starter):
            return command.replace(starter, "", 1).strip()

    for ending in endings:
        if command.endswith(ending):
            return command[:-len(ending)].strip()

    return None


class KeyboardAppOpener:
    def press(self, key):
        if key == "win":
            keyboard.press_and_release("windows")
        else:
            keyboard.press_and_release(key)

    def write(self, text, interval=0.02):
        keyboard.write(text, delay=interval)


pyautogui = KeyboardAppOpener()


def stop_speaking():
    global stop_flag
    stop_flag = True
    engine.stop()


keyboard.add_hotkey("ctrl+shift", stop_speaking)


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except:
        return ""


def ai_stream(prompt):
    global stop_flag

    process = subprocess.Popen(
        ["ollama", "run", "llama3"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )

    process.stdin.write(prompt + "\n")
    process.stdin.flush()
    process.stdin.close()

    for line in process.stdout:
        if stop_flag:
            process.kill()
            break
        yield line


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


wake_words = ["hey jarvis", "jarvis"]

while True:
    stop_flag = False

    command = listen()

    if any(w in command for w in wake_words):

        for w in wake_words:
            command = command.replace(w, "").strip()

        if command == "":
            command = listen()
            if command == "":
                continue

        print("Processing:", command)

        if open_any_app(command):
            continue

        print("Jarvis:")

        for chunk in ai_stream(command):
            if stop_flag:
                break
            print(chunk, end="", flush=True)
            speak_chunk(chunk)
