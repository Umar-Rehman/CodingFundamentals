# Saying Hello 

def say_hello():
    names = [ "Helen", "Bob", "Sarah" ] 
    for i in names:
        print(f"Hello, {i}")
    print("\n")
    names.append("Linda")
    for i in names:
        print(f"Hello, {i}")

say_hello()