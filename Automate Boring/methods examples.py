#method on a list .index() useful for finding something within a list
#these do not work on strings, only lists
spam = ['Hi', 'Hello', 'Howdy', 'Hyas']
spam.index('Hello')

#.append() and .insert() list methods
#.append - adds to end of a list
spam=['cat', 'dog', 'rat']
spam.append('bear')
print(spam)
#.insert - adds to specific location(index) in a list
spam=['cat', 'dog', 'rat']
spam.insert(1,'cow')
print(spam)

#.remove() remove an item from a list
spam=['cat', 'dog', 'cow', 'rat']
spam.remove('cow')
print(spam)

# del statement removes item at an index not the specifc value
del spam [0]
print(spam)

#lists with number or str values can be sorted
# .sort() 
spam=[2,5,-17, 3.14, 0, 24, 7]
spam.sort()
print(spam)

spam=['cat', 'dog', 'bear', 'cow', 'rat', 'elephant']
spam.sort()
print(spam)

#sorting letters in  order
#capital letters are first then lower cased
spam = ['Alice', 'Bob', 'Doug', 'charlie', 'alan']
print(spam)
spam = ['A', 'z', 'a', 'Z']
spam.sort()
print(spam)
spam.sort(key=str.lower)
print(spam)
