import webbrowser   #You may have to install these modules
import time
import os

chrome_browser = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

num = 1
while (num > 0):
    webbrowser.get(chrome_browser).open('https://www.youtube.com/watch?v=WXxV9g7lsFE') #Replace this Link with your link between the '' keys!
    time.sleep(25)
    os.system("taskkill /im chrome.exe /f") 
    time.sleep(2)
    webbrowser.get(chrome_browser).open('https://www.youtube.com/watch?v=WXxV9g7lsFE') #Replace this Link with your link between the '' keys!
    time.sleep(21) 
    os.system("taskkill /im chrome.exe /f") 
    time.sleep(3)
    webbrowser.get(chrome_browser).open('https://www.youtube.com/watch?v=WXxV9g7lsFE') #Replace this Link with your link between the '' keys!
    time.sleep(23) 
    os.system("taskkill /im chrome.exe /f") 
    time.sleep(4)
    
