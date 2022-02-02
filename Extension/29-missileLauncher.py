# Missile Launcher

# System states:
# 0 = Locked
# 1 = Partially unlocked
# 2 = Unlocked
# 3 = Armed

from time import sleep


missileDict = {"system_state" : 0, "key_insert" : "insert key", "key_remove" : "remove key", "arm" : "1234", "launch" : "fire"}

def launch_missile():
    fired = False

    while fired == False:
        
        if missileDict["system_state"] == 0:
            print(f"SYSTEM STATE: LOCKED.")
        elif missileDict["system_state"] == 1:
            print(f"SYSTEM STATE: PARTIALLY UNLOCKED.")
        elif missileDict["system_state"] == 2:
            print(f"SYSTEM STATE: UNLOCKED.")
        elif missileDict["system_state"] == 3:
            print(f"SYSTEM STATE: ARMED.")
        
        command = input("Awaiting command...\n\n")
        
        if command == missileDict["key_insert"]:
            if missileDict["system_state"] == 0:
                print(f"Key {missileDict['system_state']+1} inserted...\n")
                missileDict["system_state"] = 1
            elif missileDict["system_state"] == 1:
                print(f"Key {missileDict['system_state']+1} inserted...\n")
                missileDict["system_state"] = 2
            else:
                print("All keys already inserted...")

        elif command == missileDict["key_remove"]:
            if missileDict["system_state"] == 2:
                print(f"Key {missileDict['system_state']} removed...\n")
                missileDict["system_state"] = 1
            elif missileDict["system_state"] == 1:
                print(f"Key {missileDict['system_state']} removed...\n")
                missileDict["system_state"] = 0

        elif command == missileDict["arm"]:
            if missileDict["system_state"] < 2:
                print(f"Access Denied: Insert {2-int(missileDict['system_state'])} more key(s)...\n")
            elif missileDict["system_state"] == 3:
                print(f"Missile already armed.")
            else:
                print("Missile Armed...\n")
                missileDict["system_state"] = 3
        
        elif command == missileDict["launch"]:
            if missileDict["system_state"] < 2:
                print(f"Access Denied: Insert {2-int(missileDict['system_state'])} more key(s) then Arm Missile to Launch...\n")
            elif missileDict["system_state"] == 2:
                print(f"Access Denied: Missile must be armed before launch is possible...\n")
            else:
                print(f"WARNING! MISSILE LAUNCH IN T MINUS 5 SECONDS...\n")
                sleep(1)
                print("4")
                sleep(1)
                print("3")
                sleep(1)
                print("2")
                sleep(1)
                print("1")
                sleep(1)
                print("WARNING! MISSILE LAUNCHED! PLEASE MAKE YOUR WAY TO THE NEAREST REGISTERED BUNKER!")
                fired = True
        else:
            print(f"Access Denied: INVALID COMMAND.")
        
launch_missile()