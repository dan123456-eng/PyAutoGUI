import pyautogui
import time

for i in range(1):
    pyautogui.moveTo(100, 100, duration=0.25)
    #pyautogui.moveTo(200, 100, duration=0.25)
    #pyautogui.moveTo(200, 200, duration=0.25)
    #pyautogui.moveTo(100, 200, duration=0.25)
    
    # dar clicks
    time.sleep(15.0) # dorme por 15 segundos.
    pyautogui.click (80,80) # clica uma vez nessa cordenada.

    time.sleep(15.0)
    pyautogui.doubleClick (80,80)
    
    time.sleep(10.0)
    print("acabei de clicar!!!")
    print("coloque o mause onde quiser!")
    time.sleep(10.0)
    pyautogui.position() # Pega a posição onde o mause esta.
    print(pyautogui.position())
    pyautogui.click (pyautogui.position()); pyautogui.typewrite ('Olá mundo!') # na posição clicada sera escrito a frase ola mundo.
    print("CLIQUEI A ULTIMA VEZ!")