#Repetition and RegEx patterns
import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
mo.group()
print(mo.group())
#using batwoman
mo = batRegex.search('The Adventures of Batwoman')
mo.group()
print(mo.group())

phoneRegex= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me.')
mo.group()
print(mo.group())
#no area code
#mo = phoneRegex.search('My phone number is 555-1234. Call me.')
#mo.group()
#print(mo.group())#returns NONE

phoneRegex= re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me.')
mo.group()
print(mo.group())
mo = phoneRegex.search('My phone number is 555-1234. Call me.')
mo.group()#finds without area code
print(mo.group())


# the * means many times
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
mo.group()
print(mo.group())
#using batwoman
mo = batRegex.search('The Adventures of Batwoman')
mo.group()
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowowowowowoman')
mo.group()
print(mo.group())

# the + means most find at least once
batRegex = re.compile(r'Bat(wo)+man')
#mo = batRegex.search('The Adventures of Batman')
#mo.group() #error because it doesn't match at least once
#print(mo.group())
#using batwoman
mo = batRegex.search('The Adventures of Batwoman')
mo.group()
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowowowowowoman')
mo.group()
print(mo.group())

# how to find the literal +,*,? in the string by escaping with \
regex = re.compile(r'\+\*\?')
mo=regex.search('I Learned about +*? regex syntax')
mo.group()
print(mo.group())

#find exactly match
haRegex = re.compile(r'(Ha){3}')
haRegex.search('He said "HaHaHa"')

#find a range
haRegex = re.compile(r'(Ha){3,5}')
haRegex.search('He said "HaHaHa"')

#greedy match because of python regula programing will search for the largest match. 
digitRegex = re.compile(r'(\d){3,5}?')
digitRegex.search('1234567890')





