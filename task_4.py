#key logger 
#key logger basically log and records keystroke.
#main focus of key logger logging the key that pressed and save them into a note. 
#Ask permission to user first to avtivate key logger.

from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename=("test_file.txt"), level = logging.DEBUG, format='%(message)s : %(asctime)s')

while True:
    print("Enter 1 for give permission to user. \nEnter 2 for not giving permission.")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        def while_press(key):
            key = "{0} is pressed at ".format(key)
            logging.info(str(key))

        def while_release(key):
            if key == Key.esc:
                return False
    
        with Listener(on_press=while_press, on_release=while_release) as listener:
            listener.join()

    elif choice == 2:
        print("DO Your Work!!")
        break

    else :
        print("Invalid Choice!!")