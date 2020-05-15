#Regular Expressions
def isPhoneNumber(text):
    if len(text) != 12:
        return False #not phone number sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-': 
        return False #missing dash
    for i in range(4, 7):
        if not text[i].isdecimal(): 
            return False # no first three digits
    if text[7] != '-':
        return False #missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal(): 
            return False # last 4 digits digits
    return True

print(isPhoneNumber('415-555-1234'))
print(isPhoneNumber('Hello'))

message = ('Call me at 415-555-1101 or at my office at 415-555-9991')
foundnumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone number found: " + chunk)
        foundnumber=True
if not foundnumber:
    print('Could not find any phone numbers')