try:
    
    import cv2, pytesseract, pathlib, os, re
    from pytesseract import Output
    import PIL.Image
    import numpy as np
    import configparser
    import os.path

except:
    while True:
        print("[+] Please re-run (setup.bat) or install the requirements.txt")
        input()

config = configparser.ConfigParser()
    
def create_config():
    
    config.add_section("settings")
    config.set("settings", "tesseract_Path", r"C:\Program Files\Tesseract-OCR\tesseract.exe")
    config.set("settings", "custom_config", r"--oem 3 --psm 3")
    config.set("settings", "Debug", "False")
    
    with open("config.ini", 'w') as configfile:
        config.write(configfile)

try:
    file = open("config.ini")
    
except IOError:
    create_config()
    
def clear():
    os.system('cls')  
    
class global_vars:
    
    def __init__(self):
        pass

    config.read('config.ini')
    
    tesseractPath = config['settings']['tesseract_path']
    custom_config = config['settings']['custom_config']
    DEBUG = config['settings']['Debug']
    
    if DEBUG == True:
        
        print("\n")
        print("[+] Tesseract -> ", tesseractPath)
        print("[+] custom config -> ", custom_config)
