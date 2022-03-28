import time
import pyautogui

def sendSpamBot():
   time.sleep(5)
   text = open('word.txt')
   
   for each_line in text:
     pyautogui.typewrite(each_line)
     time.sleep(2)
     pyautogui.press('enter')
      
            
sendSpamBot()
