import pyperclip
import time
import pyautogui

text = "আপনার বার্তা"   
time.sleep(5)           

while True:
    pyperclip.copy(text)               
    pyautogui.hotkey("ctrl", "v")       
    pyautogui.press("enter")            
    time.sleep(1)                      