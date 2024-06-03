B='ctrl'
import keyboard as D,time,pyautogui as A
from mtranslate import translate as E
import pyperclip as C
while True:D.wait('f2');A.hotkey(B,'a');A.hotkey(B,'c');C.copy(E(C.paste(),'en','auto'));A.hotkey(B,'v')
