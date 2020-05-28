#Walking a Directory Tree

import os

for folderName, subfolders, filenames in os.walk('C:/Users/16787/Desktop/work'):
    print("The folder is " + folderName)
    print('The subfolders in ' + folderName + ' are:' + str(subfolders))
    print('The filenems in ' + folderName + ' are:' + str(filenames))
    print()

#examples
for subfolder in subfolders:
    if "fish" in subfolder:
        os.rmdir(subfolder)
#examples
for filename in filenames:
    if file.endswith('.py')
