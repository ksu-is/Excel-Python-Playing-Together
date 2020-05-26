# Regex sub() Method and Verbose
#ModeThe sub() regex method will substitute matches with some other text.
#Using \1, \2 and so will substitute group 1, 2, etc in the regex pattern.
#Passing re.VERBOSE lets you add whitespace and comments to the regex string passed to re.compile().
#If you want to pass multiple arguments (re.DOTALL , re.IGNORECASE, re.VERBOSE), combine them with the | bitwise operator.

import re

namesRegex =re.compile(r'Agent \w+')
mo = namesRegex.findall('Agent Alice gave the secret documents to Agent Bob')
print(mo)

mo = namesRegex.sub('REDACTED','Agent Alice gave the secret documents to Agent Bob')
print(mo)

namesRegex = re.compile(r'Agent (\w)\w*')
mo = namesRegex.findall('Agent Alice gave the secret documents to Agent Bob')
print(mo)

mo = namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob')
print(mo)#finds aparticlure items and gets first number

