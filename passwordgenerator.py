import random
import string

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation

length = int(input("Enter length: ")) 

alphabet = letters + digits + punctuation

password = "" 

for i in range(length):
    password += random.choice(alphabet) 
print("Your generated password is: ", password)    