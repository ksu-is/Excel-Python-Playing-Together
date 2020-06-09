#Regex Example Program: A Phone and Email Scraper
#this file needs a document to pull data from, the original one included with training was not 
#the same format he deonstrated during the course causing formattinmg issues

#!python3 - calls the version of Python
import re, pyperclip
#Create a Regex for phone numbers
phoneRegex=re.compile(r'''
#415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?        #area code (optinal)
(\s|-)        #first seperator
\d\d\d       #first 3 digits
-          #seperator
\d\d\d\d        #last 4 digits
(((ext(\.)?\s)|x)        # extension word-part (optional)
(\d{2,5}))?
)               # extension number-part (optional)
''', re.VERBOSE)
#Create a regex for remail adresses
emailRegex=re.compile(r'''
#some.+ thing@(\d{2,5}))?.com
[a-zA-Z0-9_.+]+  #name part
@               # @ symbol
[a-zA-Z0-9_.+]+  # domain name part
''', re.VERBOSE)
#Get the text off the clip board
text = pyperclip.paste()
#TO DO: Extract the email/phone from the text
extractedPhone = phoneRegex.findall(text)
extractedemail = emailRegex.findall(text)
#test 
#print(extractedemail)
#print(extractedPhone)

allPhonenumbers = []
for phoneNumber in extractedPhone:
    allPhonenumbers.append(phoneNumber[0])
#print(allPhonenumbers)


#Copy the extracted text to the clip board
results = '\n'.join(allPhonenumbers) + '\n' + '\n'.join(extractedemail)#this codeallows for changing the format 
#of the output data to the clipboard
pyperclip.copy(results) #text is now on the clip board
#print(results)