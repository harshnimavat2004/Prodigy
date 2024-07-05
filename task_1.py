#caesar cipher 
def encrypt(text,key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + key-65) % 26 + 65)
        else:
            result += chr((ord(char) + key-97) % 26 + 97)
    return result

def decrypt(text,key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) - key-65) % 26 + 65)
        else:
            result += chr((ord(char) - key-97) % 26 + 97)
    return result

while True :
    print("Enter 1 for fixed key operations\n Enter 2 for variable key operations\n Enter 3 for exit")
    choice = int(input("Select your choice:"))
    print()
    if choice == 1:
        key = 6
        print("key = ",key)
    elif choice == 2:
        key = int(input("Enter the key(Must be an integer): "))
        print("key = ",key)
    elif choice == 3:
        print("Thank you for using the program!")
        print("----------------------------------------------------------")
        break
    else:
        print("Invalid choice")
        break

    print("----------------------------------------------------------")
    print("Enter 1 for encryption\n Enter 2 for decryption")
    choice = int(input("Select your choice:"))
    print()
    if choice == 1:
        print("Please Enter plain text for encryption !!")
        text = str(input("Enter the plain text:"))
        print("Cipher: " + encrypt(text,key))
        print("----------------------------------------------------------")
    elif choice == 2:
        print("Please Enter cipher text for decryption !!")
        text = str(input("Enter the cipher text:"))
        print("Plain text: " + decrypt(text,key))
        print("----------------------------------------------------------")
    else:
        print("Invalid choice")
        break   
