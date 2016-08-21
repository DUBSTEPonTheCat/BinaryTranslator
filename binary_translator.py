from time import *
import string
import os
import sys
from easygui import * #fist me



            
while True:
    msg = "Mode"
    choices = ["Encrypt","Decrypt"]
    mode = buttonbox(msg, choices=choices)
    
    if "en" in mode.lower() or "1" in mode.lower():
        encrypt = 1
        decrypt = 0
    if "de" in mode.lower() or "2" in mode.lower():
        decrypt = 1
        encrypt = 0
        
    msg = "Source"
    choices = ["File","Text"]
    source = buttonbox(msg, choices=choices)
    
    
    if source == "File":
        msgbox("Please select the file you wish to translate from.")
        inputFile = fileopenbox()
        text = open(inputFile, 'r').read()
        text = text.lower()
    if source == "Text":
        msg = "Translation Source"
        title = "some shit"
        fieldNames = ["other shit"]
        fieldValues = []
        fieldValues = multenterbox(msg,title, fieldNames) 
        text = fieldValues[0]
    
    msgbox("Select the file you wish to save your translation to.")
    exportFile = fileopenbox()
    margin1 = 0
    margin2 = 9
    
    
    
    while decrypt == 1:
        exportText = ""
        text.replace(" ", "")
        print(text)
        print(text[0:9])
        print(exportText)
        print("")
        sleep(1)
            
        
        for letter in text:
            if text[0:9] == "00100000":
                exportText += " "
            elif text[0:9] == "01100001":
                exportText += "a"
            elif text[0:9] == "01100010":
                exportText += "b"
            elif text[0:9] == "01100011":
                exportText += "c"
            elif text[0:9] == "01100100":
                exportText += "d"
            elif text[0:9] == "01100101":
                exportText += "e"
            elif text[0:9] == "01100110":
                exportText += "f"
            elif text[0:9] == "01100111":
                exportText += "g"
            elif text[0:9] == "01101000":
                exportText += "h"
            elif text[0:9] == "01101001":
                exportText += "i"		
            elif text[0:9] == "01101010":
                exportText += "j"
            elif text[0:9] == "01101011":
                exportText += "k"		
            elif text[0:9] == "01101100":
                exportText += "l"
            elif text[0:9] == "01101101":
                exportText += "m"
            elif text[0:9] == "01101110":
                exportText += "n"
            elif text[0:9] == "01101111":
                exportText += "o"
            elif text[0:9] == "01110000":
                exportText += "p"
            elif text[0:9] == "01110001":
                exportText += "q"
            elif text[0:9] == "01110010":
                exportText += "r"
            elif text[0:9] == "01110011":
                exportText += "s"
            elif text[0:9] == "01110100":
                exportText += "t"
            elif text[0:9] == "01110101":
                exportText += "u"
            elif text[0:9] == "01110110":
                exportText += "v"
            elif text[0:9] == "01110111":
                exportText += "w"
            elif text[0:9] == "01111000":
                exportText += "x"
            elif text[0:9] == "01111001":
                exportText += "y"
            elif text[0:9] == "01111010":
                exportText += "z"
            elif text[0:9] == "00110000":
                exportText += "0"
            elif text[0:9] == "00110001":
                exportText += "1"
            elif text[0:9] == "00110010":
                exportText += "2"
            elif text[0:9] == "00110011":
                exportText += "3"
            elif text[0:9] == "00110100":
                exportText += "4"
            elif text[0:9] == "00110101":
                exportText += "5"
            elif text[0:9] == "00110110":
                exportText += "6"
            elif text[0:9] == "00110111":
                exportText += "7"
            elif text[0:9] == "00111000":
                exportText += "8"
            elif text[0:9] == "00111001":
                exportText += "9"
            else:
                exportText += "."
            
    if encrypt == 1:
            
        
        exportText = ""

        for letter in text:
            if letter == chr(ord(" ")):
                exportText += " 00100000"
            elif letter == "a":
                exportText += " 01100001"
            elif letter == "b":
                exportText += " 01100010"
            elif letter == "c":
                exportText += " 01100011"
            elif letter == "d":
                exportText += " 01100100"
            elif letter == "e":
                exportText += " 01100101"
            elif letter == "f":
                exportText += " 01100110"
            elif letter == "g":
                exportText += " 01100111"
            elif letter == "h":
                exportText += " 01101000"
            elif letter == "i":
                exportText += " 01101001"		
            elif letter == "j":
                exportText += " 01101010"
            elif letter == "k":
                exportText += " 01101011"		
            elif letter == "l":
                exportText += " 01101100"
            elif letter == "m":
                exportText += " 01101101"
            elif letter == "n":
                exportText += " 01101110"
            elif letter == "o":
                exportText += " 01101111"
            elif letter == "p":
                exportText += " 01110000"
            elif letter == "q":
                exportText += " 01110001"
            elif letter == "r":
                exportText += " 01110010"
            elif letter == "s":
                exportText += " 01110011"
            elif letter == "t":
                exportText += " 01110100"
            elif letter == "u":
                exportText += " 01110101"
            elif letter == "v":
                exportText += " 01110110"
            elif letter == "w":
                exportText += " 01110111"
            elif letter == "x":
                exportText += " 01111000"
            elif letter == "y":
                exportText += " 01111001"
            elif letter == "z":
                exportText += " 01111010"
            elif letter == "0":
                exportText += " 00110000"
            elif letter == "1":
                exportText += " 00110001"
            elif letter == "2":
                exportText += " 00110010"
            elif letter == "3":
                exportText += " 00110011"
            elif letter == "4":
                exportText += " 00110100"
            elif letter == "5":
                exportText += " 00110101"
            elif letter == "6":
                exportText += " 00110110"
            elif letter == "7":
                exportText += " 00110111"
            elif letter == "8":
                exportText += " 00111000"
            elif letter == "9":
                exportText += " 00111001"
            else:
                exportText += "."

        print(exportText)
        if source == "File":
            Export = open(exportFile, "w+")
            Export.write(exportText)
        textbox(exportText)
