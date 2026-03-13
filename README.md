# Windows Jarvis AI Assistant

A customizable voice-controlled desktop assistant built using Python that can automate system tasks, control applications, search files, and provide AI-powered responses locally.

This assistant is designed as a productivity tool capable of managing applications, executing system commands, searching files efficiently, and interacting with the user through voice responses.

---

## Key Features

### Memory System
Jarvis can remember information and store it in a JSON file for later retrieval.

### Application Control
Open applications installed on the system using their name or Windows-recognized search terms.

### Application Management
Close specific applications or multiple applications simultaneously.

### Smart Internet Search
Search directly on:
- Google
- YouTube
- Wikipedia
- General web queries

### Advanced File & Folder Search
Locate and open files or folders efficiently even when multiple files have the same name.

### Website Launcher
Quickly open predefined websites using voice or command input.

### System Control Commands
Execute system-level commands such as:

- Shutdown
- Restart
- Lock system
- Sleep mode
- Task Manager
- Control Panel

Additional commands can easily be added.

### Screen Reading Capability
Jarvis can capture the screen, convert the screenshot to text using OCR, and allow the user to ask questions based on the extracted text.

### Local AI Integration
Jarvis can generate AI responses using a locally running DeepSeek-R1:7B model.

### Custom Productivity Modes
Jarvis supports custom work modes that automatically prepare the system environment.

Examples:

- Python Mode
- Java Mode
- UI Mode
- Gaming Mode

Each mode closes unnecessary applications and opens the required tools for that workflow.

### Voice Feedback
Jarvis provides voice responses to confirm commands and interact with the user.

---

## Technologies Used

- Python
- SpeechRecognition
- Whisper (OpenAI)
- Pyttsx3
- PyAutoGUI
- Pytesseract (OCR)
- JSON (Memory Storage)
- OS & Subprocess Modules
- Local AI Model (DeepSeek-R1:7B)

---

## Installation

1. Clone the repository
   https://github.com/mohdsaadkhan073/Windows-Jarvis-AI-Assistant.git

2. Install Dependencies
   py -3.11 pip -m install -r requirements.txt

3. Run the Assistant
   py -3.11 jarvis.py


---

## Important Note

Some application paths inside the script may need to be updated according to your system configuration.

---

## Future Improvements

- Graphical User Interface (GUI)
- Better command recognition
- Cross-platform support
- More AI integrations

---

## Author

Mohd Saad Khan  
Diploma in Computer Engineering

