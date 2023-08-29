import pyautogui
import keyboard
import time
import random
import win32api, win32con

automatorSetting=0
scriptActive=1
stepNumber=0
inGameY=0
targetCoords=0

   #elif event.event_type == 'down':
       # print(f"{event.name} key was pressed")

while True: 
    event = keyboard.read_event()

    if keyboard.is_pressed('=') == True:
        scriptActive = 0
        print("scriptActive")

    if keyboard.is_pressed('-') == True:
        scriptActive = 1
        print("script deactivated")

    if keyboard.is_pressed('0') == True and scriptActive == 0:
        automatorSetting=0
        print("automator off")

    if keyboard.is_pressed('1') == True and scriptActive == 0:
        automatorSetting=1
        print("setting 1")

    if keyboard.is_pressed('2') == True and scriptActive == 0:
        automatorSetting=2
        print("setting 2")

    if keyboard.is_pressed('3') == True and scriptActive == 0:
        automatorSetting=3
        print("setting 3")

    while automatorSetting == 1 and keyboard.is_pressed('0') == False:
           pyautogui.keyDown('q')
           pyautogui.keyDown('w')

    while automatorSetting == 2 and keyboard.is_pressed('0') == False:
        print("2")
        time.sleep(0.1)
        pyautogui.write('enter')
        pyautogui.click(clicks=1, interval=1)
        with pyautogui.keyDown('w'):
            pyautogui.click(clicks=1, interval=1)
        with pyautogui.hold('shift'):
            pyautogui.press('esc')
        pyautogui.keyDown('w')
        pyautogui.leftClickduration = 10

    if automatorSetting == 3 and keyboard.is_pressed('0') == False:
         
        stepNumber=1


    if stepNumber == 1:
        if pyautogui.locateOnScreen('targetY.png', confidence=0.7) != None:
           print("found it")
           stepNumber=2
        else:
            pyautogui.keyDown('q')
            print("no found it")
            
    if stepNumber == 2:
       #epic camera movement
       pyautogui.keyDown('l')
       while targetCoords == 0:
            pyautogui.keyDown('w')
            if pyautogui.locateOnScreen('targetCoords.png', confidence=0.7) != None:
                targetCoords = 1
                print("found it")
       else:
           print("found it 2")
           stepNumber=3

   # if stepNumber == 3:
  
