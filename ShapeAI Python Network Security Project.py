# importing hashlib package to perform md5 encryption
import hashlib
# accepting the string from user to be hashed
hashing = input("Enter the string to be md5 hashed:- ")
# hashing the string
hashed = hashlib.md5(hashing.encode())
# printing the Byte Equivalent of Hash
print("The byte equivalent of hash is : ", hashed.digest())
# printing the Hexadecimal Equivalent of Hash
print("The hexadecimal equivalent of hash is : ", hashed.hexdigest())