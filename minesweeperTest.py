import pyautogui


for p in pyautogui.locateAllOnScreen('one.png',confidence=0.99):
    pos=pyautogui.center(p)
    print(pos)
