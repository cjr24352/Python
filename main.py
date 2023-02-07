import string
def caesar_cipher(message, key):
    s = ""
    alphabet = string.ascii_letters + string.digits + string.punctuation + " "
    for letter in message:
        if letter in " ~`!@#$%^&*()+_-={}|[]\:;,./<>?":
            s = s + letter
        else:
            s = s + alphabet[(alphabet.index(letter) + key) % 62]
    print(s)

message = input("Enter the message which has to be encrypted or decrypted : ")
mode = input("Enter the mode whether to be encrypt or decrypt : ")
key = int(input("Enter the key value to shift the values : "))
if mode == "encrypt" or mode == "ENCRYPT" or mode == "E" or mode == "e":
    caesar_cipher(message, key)
elif mode == "decrypt" or mode == "DECRYPT" or mode == "D" or mode == "d":
    key = - key
    caesar_cipher(message, key)
else:
  print("Please make sure you entered everything correctly!")