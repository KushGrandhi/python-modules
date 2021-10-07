import pyttsx3 as py3
import os
import time

py3.speak("Welcome Pranav")
py3.speak("Welcome to your personal assistant")
py3.speak("Please specify your operation")

while True:
    print()
    print("We Support following Text Editors and following Social Media Applications")
    print()
    print("1. Notepad")
    print("2. WordPad")
    print("3. Textpad")
    print("4. Facebook")
    print("5. Youtube")
    print("6. LinkedIN")
    print()
    print("Supported browser and Other Applications are below..")
    print()
    print("1. Chrome")
    print("2. DockerHub")
    print("3. Google Cloud Platform") 		
    print("4. Oracle VirtualBox")	
    print("5. Google")
    print("6. Calculator") 
    print("7. Media Player") 
    print("8. Windows Explorer")
    print("9. VS code")
    print("10. OBS studio")
    print("11. WhatsApp")
    print("12. Zoom")
    print("13. Spyder (Anaconda)")
    print("____________________________________________________________________________________________________________________________") 
    print("Please specify your operation: ",end='')
    command = input()

    os.system("cls")
    if ("chrome" in command):
        os.system("start chrome")
    elif ("wmplayer" in command) or ("mediaplayer" in command):
        os.system("start wmplayer")
    elif ("notepad" in command):
        os.system("start notepad")
    elif("paint" in command):
        os.system("start mspaint")
    elif ("calculator" in command) or ("cal" in command):
        os.system("start calc")
    elif ("command" in command) or ("cmd" in command):
        os.system("start cmd")
    elif ("file" in command):
        os.system("start explorer")
    elif ("virtual" in command):
        os.system("start VirtualBox")
    elif ("vscode" in command):
        os.system("start Code")
    elif ("word" in command):
        os.system("start WINWORD")
    elif ("ppt" in command):
        os.system("start POWERPNT")
    elif ("vm" in command) or ("virtual" in command) or ("vbox" in command):
        os.startfile("C:/Program Files/Oracle/VirtualBox/VirtualBox.exe")
    elif ("spotify" in command):
        os.startfile("C:/Users/Pranav/AppData/Roaming/Spotify/Spotify.exe")
    elif("zoom" in command):
        os.startfile("C:/Users/Pranav/AppData/Roaming/Zoom/bin/Zoom.exe")
    elif ("spyder" in command) or ("anaconda" in command):
        os.startfile("C:/Users/Pranav/anaconda3/pythonw.exe")
    elif ("Whatsapp" in command) or ("whats" in command):
        os.startfile("C:/Users/Pranav/AppData/Local/WhatsApp/WhatsApp.exe")
    elif ("obs" in command) or ("studio" in command):
        os.startfile("C:/Program Files/obs-studio/bin/64bit/obs64.exe")
    elif ("google" in command):
        os.system('start chrome "https://www.google.com" --kiosk')
    elif ("youtube" in command):
        os.system('start chrome "https://www.youtube.com" --kiosk')
    elif ("gcp" in command) or ("cloud" in command):
        os.system('start chrome "https://cloud.google.com" --kiosk')
    elif ("linkedin" in command):
        os.system('start chrome "https://www.linkedin.com" --kiosk')
    elif ("docker" in command):
        os.system('start chrome "https://hub.docker.com" --kiosk')
    elif ("quit" in command) or ("exit" in command) or ("bye" in command):
        py3.speak("Have a great day ahead")

    else:
        py3.speak("Sorry we do not suppport your specified choice")
