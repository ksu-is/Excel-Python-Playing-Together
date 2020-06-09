list('Hello')
name =['Zophie']
name[0]

for letter in name:
    print(letter)

#mutable and imutable data types
#lists are mutable - items can be chnaged added removed deleted etc
#imutable strings cannot be modified in place but must be replaced - not stored inside but refernced
# this is a refernce
def eggs(cheese):
    cheese.append('Hello')
spam=[1,2,3]
eggs(spam)
print(spam)

#to create a seperate list that can be modified
import copy
spam=['A', 'B', 'C', 'D']
cheese=copy.deepcopy(spam)
cheese[1] = 42
print(cheese)
print(spam)


#line contimnuation
spam=['apples', 'oranges', 
    'pears',
    'pulms',
    'eggs']
print(spam)

print('four score and' + \
        'seven years ago')
