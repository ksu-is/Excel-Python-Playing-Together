#store in a shelf file

import shelve
shelfFile=shelve.open('my data')
shelfFile['cats'] = ['Zophie','carl','sammy','jimmie']

shelfFile.close()


shelfFile=shelve.open('my data')
shelfFile.keys()
mo = list(shelfFile.keys())
print(mo)
shelfFile.close()

shelfFile=shelve.open('my data')
shelfFile.values()
mo = list(shelfFile.values())
print(mo)
shelfFile.close()