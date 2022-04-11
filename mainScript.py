from senders import sender
import receivers

if __name__ == "__main__":
    run = True
    while run == True:
        action = input(
            'Enter 1 for sending message \nEnter 2 for getting the nessage for specific receiver\n3 - for exit ')
        if (action == "3"):
            run = False
            exit(0)
        elif (action == "1"):
            name = input('Enter sender\'s name ')
            receiver = input('Enter receiver\'s name ')
            message = input('Enter the message ')
            sender([name, receiver, message])
        elif (action == "2"):
            name_receiver = input('Enter receiver\'s name ')
            receivers.main(name_receiver)
        else:
            print("wrong input")
    exit(0)
