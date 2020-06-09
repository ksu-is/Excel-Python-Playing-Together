# Regular Expressions 2
import re

message = ('Call me at 415-555-1101 or at my office at 415-555-9991')

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Call me at 415-555-1101 or at my office at 415-555-9991')
print(mo.group())

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('Call me at 415-555-1101 or at my office at 415-555-9991'))
