# Simple encryption and decryption

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
            new_str+=str(chr(i+101))
        else:
            new_str+=str(chr(i+75))
    print(new_str)    
    return new_str

encrypt()