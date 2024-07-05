#Password Complexity Checker
print("Password Complexity Checker")
print("-------------------------------------------")
print("Password must conatin below prerequisites :\n1. Password length should be greater than  or equal to 8\n2. Password should contain atleast one digit\n3. Password should contain atleast one uppercase letter\n4. Password should contain atleast one lowercase letter\n5. Password should contain atleast one special characterfsr")
import string
password = str(input("Enter Your Password : "))
def password_check(password):
    if len(password) < 8:
        return False            #Password length should be greater than 8
    if not any(char.isdigit() for char in password):
        return False            #Password should contain atleast one digit
    if not any(char.isupper() for char in password):
        return False            #Password should contain atleast one uppercase letter
    if not any(char.islower() for char in password):
        return False            #Password should contain atleast one lowercase letter
    if not any(char in string.punctuation for char in password):
        return False            #Password should contain atleast one special character
    return True
if password_check(password):
    print("Password is Strong")
else:
    print("Password is Weak")
