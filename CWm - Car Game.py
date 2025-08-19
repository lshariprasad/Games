command = ""

started = False

while True:
    command = input ("> ").lower()

    if command == "help" :
        print(" start - to start the car ")
        print(" stop - to stop the car ")
        print(" quit - to exit ")

    elif command == "start" :
        if started:
            print("Car is alreday Started!")
        else:
            started = True    
            print ("Car Started...Ready to go!")

    elif  command == "stop" : 
        if not started:
            print("Car is Already stopped!")
        else:
            started = False
            print ("Car Stopped.")

    elif command == "quit" :
        print ("You are Exit Form the Game...")
        break

    else :
        print ("Invalid Commend... ")