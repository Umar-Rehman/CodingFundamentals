import string
import random

def generate_password():
    secure = False

    while secure == False:
        all = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.sample(all,10))

        if ((any(char.isupper() for char in password) and any(char.islower() for char in password) 
            and any(char.isdigit() for char in password) and any(char in string.punctuation for char in password))):
            secure = True
        else:
            continue

    print(password)
    return(password)