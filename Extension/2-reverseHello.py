# Saying Hello, in Reverse

def say_hello_reversed():
    names = [ "Helen", "Bob", "Sarah" ]
    for i in reversed(names):
        print(f"Hello, {i}")

say_hello_reversed()