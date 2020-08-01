help = """
help - to show this menu
start - to start the car
stop - to stop the car
quit - to exit
"""
print(help)
command = ''
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Hey, Car already started!")
        else:
            print("Car started, ready to go!")
            started = True
    elif command == "stop":
        if not started:
            print("Hey, Car already stopped!")
        else:
            print("Car stopped")
            started = False
    elif command == "help":
        print(help)
    elif command == 'quit':
        break
    else:
        print("I donot understand that")
