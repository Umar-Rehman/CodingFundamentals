# Simple encryption and decryption

import re

def encrypt():
    string = input("Enter a message: ").lower()

    numbers = [ord(letter) - 96 for letter in string]

    new_str = ""
    for i in numbers:
        if (i+96 < 192 and i+96 > 159) or (i+96>122 and i+96<127) or (i+96>90 and i+96<97) or (i+96>57 and i+96<65) or (i+96>31 and i+96<48):
            new_str+=str(chr(i+96))
        elif i+96 == 32:
            new_str+=" "
        elif i+96 < 118:
            if i+96 > 57:
                new_str+=str(chr(i+101))
            elif i+96 > 52:
                new_str+=str(chr(i+91))
            else:
                new_str+=str(chr(i+101))
        else:
            new_str+=str(chr(i+75))
    print(new_str)    
    return new_str

encrypt()

def decrypt():
    string = input("Enter a message: ").lower()
    numbers = []
    new_str = ""
    for i in string:
        if (ord(i)< 192 and ord(i)> 159) or (ord(i)>122 and ord(i)<127) or (ord(i)>90 and ord(i)<97) or (ord(i)>57 and ord(i)<65) or (ord(i)>31 and ord(i)<48):
            numbers.append(ord(i))
        elif bool(i.isalpha) == True and ((ord(i)-96) > 5):
            numbers.append(ord(i)-101)
        elif bool(i.isalpha) == True and ((ord(i)-96) < 5):
            numbers.append(ord(i)-75)
        elif ord(i) == 32:
            numbers.append(" ")
        elif bool(i.isdigit) == True:
            numbers.append(ord(i)-53)
        
    for i in numbers:
        if (i< 192 and i> 159) or (i>122 and i<127) or (i>90 and i<97) or (i>57 and i<65) or (i>31 and i<48):
            new_str+=str(chr(i))
        elif i > 26:
            new_str+=str(chr(i+74))
        elif i == -43:
            new_str+=" "
        elif i < -17 and i > -28:
            if i+75 > 52:
                new_str+=str(chr(i+70))
            else:
                new_str+=(str(chr(i+80)))
        else:
            new_str+=str(chr(i+96))
    print(new_str)

decrypt()