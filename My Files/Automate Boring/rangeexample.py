#for i in range(4):
    #print(i)


#[0,1,2,3,4]
#for i in [0,1,2,3,4]:
    #print(i)

spam = list(range(0,100,2))
print(spam)

supplies = ['pens', 'paper', 'flamethrower', 'pencils']
for i in range(len(supplies)):
        print('index ' + str(i) + ' in supplies is :' + supplies[i])

supplies= ['pens', 'pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens']
for i in range(len(supplies)):
        print('index ' + str(i) + ' in supplies is :' + supplies[i]) 

cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
print(size, color, disposition)

size, color, disposition=cat
print(size, color, disposition)

size, color, disposition= ['skinny', 'black', 'quiet']
print(size, color, disposition)
#swapping variables
a = 'AAA'
b = 'BBB'
a,b = b, a
print(a,b)

#augmented assignemnt opeartors create shortcuts
spam = 42
spam = spam +1
print(spam)
spam+=1
print(spam)
