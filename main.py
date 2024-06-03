import keyboard
import time
import pyautogui
from mtranslate import translate
import pyperclip #импортируем весь мусор
hotkey = input("Горячая клавиша:") #задаем хоткей
destln = input("Итоговый язык(en, ru, de...):") #задаём язык
while True:
 keyboard.wait(hotkey) #ждем нажатия хоткея
 pyautogui.hotkey('ctrl', 'a') #выделяем
 pyautogui.hotkey('ctrl', 'c') #копируем
 pyperclip.copy(translate(pyperclip.paste(),destln,"auto")) #переводим
 pyautogui.hotkey('ctrl', 'v') #вставляем
 print("Переведено") #для понятности выводим сообщение
