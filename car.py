"""
    This ia a multi line comment.
"""
command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "help":
        print(""" 
    start - to start the car
    left - to turn left
    right - to turn right
    stop - to stop the car
    quit - to quit the game
        """)
    elif command == "start":
        if started:
            print("Car has already started!")
        else:
            started = True
            print("The car started...")
    elif command == "stop":
        if not started:
            print("Car has already stopped!")
        else:
            started = False
            print("The car stopped|||")
    elif command == "left":
        print("Car turned left <--")
    elif command == "right":
        print("Car turned right -->")
    elif command == "quit":
        print("***OVER***")
        break 
    else:
        print("Sorry, I don't understand.")