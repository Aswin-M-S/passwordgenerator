import random
import string

num = int(input("enter the length of the password: "))

def password_generaotr(num):
    password = ""
    for n in range(num):
        x = random.randint(0,94)
        password += string.printable[x]
    return password
print(password_generaotr(num))
