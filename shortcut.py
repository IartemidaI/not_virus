import os, winshell
from win32com.client import Dispatch
# Получаем путь до рабочего стола.
desktop = winshell.desktop()
# Соединяем пути, с учётом разных операционок.
path = os.path.join(desktop, "Fox.lnk")
# Задаём путь к файлу, к которому делаем ярлык.
target = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
# Назначаем путь к рабочей папке.
wDir = r"C:\Program Files (x86)\Mozilla Firefox"
# Путь к нужной нам иконке.
icon = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
# С помощью метода Dispatch, обьявляем работу с Wscript (работа с ярлыками, реестром и прочей системной информацией в windows)
shell = Dispatch('WScript.Shell')
# Создаём ярлык.
shortcut = shell.CreateShortCut(path)
# Путь к файлу, к которому делаем ярлык.
shortcut.Targetpath = target
# Путь к рабочей папке.
shortcut.WorkingDirectory = wDir
# Тырим иконку.
shortcut.IconLocation = icon
# Обязательное действо, сохраняем ярлык.
shortcut.save()
