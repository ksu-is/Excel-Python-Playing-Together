#Regex Dot-Star and the Caret/Dollar Characters

import re

beginsWithHelloRegex = re.compile(r'^Hello')
beginsWithHelloRegex.search('Hello there!')#matches bexause it starts with Hello
beginsWithHelloRegex.search('He said, Hello there!')# does not match as it doesnt start with Hello 
beginsWithHelloRegex.search('He said, Hello there!') == None

endsWithHelloRegex = re.compile(r'world!$')# searches for exact match at end of string
endsWithHelloRegex.search('Hello world!')# must matcth the entire string

allDigitsRegex = re.compile(r'^\d+$')
allDigitsRegex.search('35462728949366375')#match becuase it begins and ends with the pattern
allDigitsRegex.search('35462728xx949366375')#does not match, it does not begin and end with the pattern

atRegex = re.compile(r'.at')#finds any charatcter except a new line, including white space
mo = atRegex.findall('The cat in the hat sat at the flat mat')
print(mo)

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')# wildcard serach - greedy match
bo = nameRegex.findall("First Name: Al Last Name: Sweigert")
print(bo)

serve = '<to serve humans> for dinner.>'

nongreedy = re.compile(r'<(.*?)>')
mo = nongreedy.findall(serve)
print(mo)

greedy = re.compile(r'<(.*)>')
mo = greedy.findall(serve)
print(mo)

prime="Serve the public trust\nProtect the innocent \nUphold the law"
print(prime)
dotStar = re.compile(r'.*')#finds the first then stops
bo = dotStar.search(prime)
print(bo)

dotStar = re.compile(r'.*', re.DOTALL) #continues to search
aoc = dotStar.search(prime)
print(aoc)
