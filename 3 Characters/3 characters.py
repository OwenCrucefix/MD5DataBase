from hashlib import *
enc = md5()
words = open("3 characters.txt","w")
encrypt = open("3 characters hex encrypted.txt","w")
word = "   "
x = 0
y = 0
z = 0
words.write(word + "\n")
enc.update(word)
encrypt.write(enc.hexdigest()+"\n")
try:
    while x != 95:    
        while y != 95:
            while z != 94:
                word = word[0] + word[1] + chr(ord(word[2])+1)
                z += 1
                words.write(word + "\n")
                enc.update(word)
                encrypt.write(enc.hexdigest()+"\n")
            z = 0
            word = word[0] + word[1] + " "
            word = word[0] + chr(ord(word[1])+1) + word[2]
            y += 1
        y = 0
        word = word[0] + " " + " "
        word = chr(ord(word[0])+1) + word[1] + word[2]
        x += 1
except IndexError:
    words.close()
    
words.close()
encrypt.close()
"""
list =[]
allwords = open("3 letters.txt","r")
for i in allwords:
    list.append(i)
print list
"""
