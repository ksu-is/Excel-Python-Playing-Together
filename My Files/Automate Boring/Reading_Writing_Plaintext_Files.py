#Reading and Writing Plaintext Files

helloFile = open('C:/Users/16787/Desktop/waffles/Helloworld.txt') #opens file in read mode
content = helloFile.read()
helloFile.close()

helloFile = open('C:/Users/16787/Desktop/waffles/Helloworld.txt') #opens file in read mode
helloFile.readlines()
helloFile.close()
print(content)

#opens and creates a new file to write
helloFile = open('C:/Users/16787/Desktop/waffles/Helloworld2.txt', 'w')
helloFile.write("Hello!!!!!!!!\n")

helloFile.write("Hello!!!!!!!!\n")#adds new line

helloFile.write("Hello!!!!!!!!\n")

helloFile.write("Hello!!!!!!!!\n")
helloFile.close()#created Helloworld2 yext file and wrote

baconFile = open('bacon.txt', 'w')
baconFile.write('Bacon is not a vegtable')

baconFile.close()

import os

os.getcwd()
print(os.getcwd())

baconFile = open('bacon.txt', 'a')
baconFile.write('\n\nBacon is delicious')

baconFile.close()

