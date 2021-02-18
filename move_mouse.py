
import pyautogui
 
screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth /9, screenHeight / 2)
 
print(pyautogui.size())