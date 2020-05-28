#Filenames and Absolute/Relative File Paths

import os


mo = os.path.join('floder1', 'folder2', 'folder3', 'spam.png')
print(mo)
bo = os.sep
print(bo)

bo = os.getcwd()
print(bo)

bo = os.chdir('c:\\')
print(bo)

os.path.exists('c:\\windows\\systems32\\calc.exe')

os.path.isfile('c:\\windows\\systems32\\calc.exe')

os.path.isdir('c:\\windows\\systems32\\calc.exe')

os.path.exists('c:\\windows\\system32\\calc.exe')

os.path.isfile('c:\\windows\\system32\\calc.exe')

os.path.isdir('c:\\windows\\system32\\calc.exe')

os.path.getsize('c:\\windows\\system32\\calc.exe')

mo = os.listdir('C:/Users/16787/Desktop')
print(mo) #lists all of the directories in the folder desktop


totalSize = 0
for filename in os.listdir('C:/Users/16787/Desktop'):
    if not os.path.isfile(os.path.join('C:/Users/16787/Desktop', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('C:/Users/16787/Desktop', filename))
print(totalSize)

os.makedirs('C:/Users/16787/Desktop/waffles/walnuts/yummy')# makes folders