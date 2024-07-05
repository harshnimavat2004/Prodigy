# Pixel manipulation for Image encryption and decryption
import numpy as np 
import cv2 

def encrypt(image, key):
    # Load the image
    img = cv2.imread(image)
    # Get the shape of the image
    shape = img.shape
    # Get the key
    key = int(key) # key is the pixel value to be XORed with the image pixels
    # Encrypt the image
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(shape[2]):
                img[i][j][k] = img[i][j][k] ^ key
    # Save the encrypted image
    cv2.imwrite('encrypted_image.png', img)
    # show the encrypted image
    cv2.imshow('Encrypted Image', img)
    cv2.waitKey(0)

def decrypt(image, key):
    # Load the image
    img = cv2.imread(image)
    # Get the shape of the image
    shape = img.shape
    # Get the key
    key = int(key)
    # Decrypt the image
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(shape[2]):
                img[i][j][k] = img[i][j][k] ^ key
    # Save the decrypted image
    cv2.imwrite('decrypted_image.png', img)
    # show the decrypted image
    cv2.imshow('Decrypted Image', img)
    cv2.waitKey(0)

image = 'testimg.jpg'
image2 ='encrypted_image.png'
while True:
    print("Enter 1 for encryption\nEnter 2 for decryption\nEnter 3 for exit")
    choice = int(input("Select your choice:"))
    print()
    if choice == 1:
        key = input("Enter the key: ")
        encrypt(image, key)
    elif choice == 2:
        if not image2:
            print("No encrypted image found")
            break
        key = input("Enter the key: ")
        decrypt(image2, key)
    elif choice == 3:
        print("Thank you for using the program!")
        print("----------------------------------------------------------")
        break
    else:
        print("Invalid choice")
        break