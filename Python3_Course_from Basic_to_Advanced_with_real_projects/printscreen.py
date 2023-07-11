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
    # Selecionado area (tela)
    # pyautogui.moveTo(x=3993, y=1060, duration=0.1)
    # pyautogui.leftClick()
    # pyautogui.moveTo(x=3866, y=1009, duration=0.1)
    # pyautogui.leftClick()
    # pyautogui.moveTo(x=4460, y=583, duration=0.1)
    # pyautogui.leftClick()

    # Selecionado area (pagina 1)
    pyautogui.moveTo(x=2011, y=1065, duration=0.1)
    pyautogui.leftClick()
    pyautogui.moveTo(x=937, y=1010, duration=0.1)
    pyautogui.leftClick()
    pyautogui.moveTo(x=77, y=135, duration=0.1)
    pyautogui.mouseDown(x=77, y=135, button='left')
    pyautogui.moveTo(x=1279, y=1036, duration=0.1)
    pyautogui.mouseUp(x=1279, y=1036, button='left')
    pyautogui.moveTo(x=1205, y=102, duration=0.1)
    pyautogui.leftClick()

    # Selecionado area (pagina 2)
    pyautogui.moveTo(x=2011, y=1065, duration=0.1)
    pyautogui.leftClick()
    pyautogui.moveTo(x=937, y=1010, duration=0.1)
    pyautogui.leftClick()
    pyautogui.moveTo(x=1334, y=132, duration=0.1)
    pyautogui.mouseDown(x=1334, y=132, button='left')
    pyautogui.moveTo(x=2525, y=1026, duration=0.1)
    pyautogui.mouseUp(x=2525, y=1026, button='left')
    pyautogui.moveTo(x=2454, y=99, duration=0.1)
    pyautogui.leftClick()
    pyautogui.moveTo(x=2535, y=578, duration=0.1)
    pyautogui.leftClick()
