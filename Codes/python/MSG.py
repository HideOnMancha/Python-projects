import pyautogui as py
import random
import time
time.sleep(2)
mensagens = ('LARISSA', "LARISSA", 'LARISSA')
for i in range(1):
    msg = random.choice(mensagens)
    py.write(msg)
    py.press('enter')

