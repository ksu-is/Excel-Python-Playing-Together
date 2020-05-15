#string formatting
name = 'Alice'
place= 'Main street'
time = '6pm'
food = 'turnips'
print('Hello ' + name + ' you are invited to a party at ' + place + ' at ' + time +'. Please bring ' + food + '.')
#%(name, place, time, food)
print('Hello %s you are invited to a party at %s at %s. Please bring %s.' %(name, place, time, food))