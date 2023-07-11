# pip install pyautogui pillow mouseinfo (cmd windows)
# python (cmd)
# from mouseinfo import mouseInfo (cmd) => para ver a coordenada do mouse
# mouseInfo()
# Desmarcar (2 sec. Button Delay)
# Para gravar a coordenada apertar F6
import pyautogui

# Tela toda
# pyautogui.moveTo(x=3992, y=1068, duration=2)
# pyautogui.leftClick()
# pyautogui.moveTo(x=3326, y=1008, duration=2)
# pyautogui.leftClick()
# pyautogui.moveTo(x=3842, y=1004, duration=2)
# pyautogui.leftClick()
# pyautogui.moveTo(x=4433, y=537, duration=2)
# pyautogui.leftClick()

try:
    pages = int(input('Insert how many pages do you intend to print: '))
except (ValueError, NameError):
    print('Insert only integer number!')

for i in range(pages):

    # Selecionado area (pagina 1)
    pyautogui.moveTo(x=3980, y=1065, duration=0.1)
    pyautogui.leftClick()
    pyautogui.moveTo(x=3186, y=1008, duration=0.1)
    pyautogui.leftClick()
    pyautogui.moveTo(x=2644, y=97, duration=0.1)
    pyautogui.mouseDown(x=2644, y=97, button='left')
    pyautogui.moveTo(x=3539, y=1044, duration=0.1)
    pyautogui.mouseUp(x=3539, y=1044, button='left')
    pyautogui.moveTo(x=3493, y=69, duration=0.1)
    pyautogui.leftClick()

    # # Selecionado area (pagina 2)
    pyautogui.moveTo(x=3980, y=1065, duration=0.1)
    pyautogui.leftClick()
    pyautogui.moveTo(x=3186, y=1008, duration=0.1)
    pyautogui.leftClick()
    pyautogui.moveTo(x=3572, y=101, duration=0.1)
    pyautogui.mouseDown(x=3572, y=101, button='left')
    pyautogui.moveTo(x=4451, y=1029, duration=0.1)
    pyautogui.mouseUp(x=4451, y=1029, button='left')
    pyautogui.moveTo(x=4337, y=58, duration=0.1)
    pyautogui.leftClick()
    pyautogui.moveTo(x=4446, y=570, duration=0.1)
    pyautogui.leftClick()
