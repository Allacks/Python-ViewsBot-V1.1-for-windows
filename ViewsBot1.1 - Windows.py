import webbrowser   
import time
import os
import threading

num = 1
Browser = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

    
def watch():
    webbrowser.get(Browser).open('https://www.youtube.com/watch?v=WXxV9g7lsFE')
 

def threadA():
    threading.Thread(target=watch).start()

def LoopIt():
   threadA() 
   time.sleep(25)
   os.system("taskkill /im chrome.exe /f") 
   time.sleep(2)
   threadA()    
   time.sleep(21) 
   os.system("taskkill /im chrome.exe /f")
   time.sleep(3)
   threadA()
   time.sleep(23)
   os.system("taskkill /im chrome.exe /f")
   time.sleep(2)
   LoopIt()

LoopIt()
