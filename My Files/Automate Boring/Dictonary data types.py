#Dictonary data types- keys:values
myCat ={'size':'fat', 'color':'blue', 'dispostion':'sneaky'}
print(myCat['size'])
print('My Cat has ' + myCat['color'], 'fur')

#dictonraies have no order
#must run in shell to visualize
[1,2,3]==[3,2,1]

eggs={'species':'cat', 'color':'blue', 'disposition':'ugly'}
ham= {'disposition':'ugly','species':'cat','color': 'blue'}
eggs==ham

list(eggs.keys())
list(eggs.values())
list(eggs.items())
eggs.keys()

for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for k, v in eggs.items():
    print(k,v)

if 'color' in eggs:
    print(eggs['color'])

eggs.get('color', 0)
eggs.get('age', '')

picnicitems = {'cups': 15, 'Napkins':35}
print('I am bringing ' + str(picnicitems.get('Napkins', 0, ))+ ' to the picnic')

eggs={'species':'cat', 'color':'blue', 'disposition':'ugly'}
# 'age' not in eggs:
    #eggs('age') = 8
    #print(eggs)

eggs.setdefault('age','8')
print(eggs)


