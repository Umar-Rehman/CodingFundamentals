# 4. Blast off 

import time

def blast_off():
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)
    print("Blast Off!")

blast_off()