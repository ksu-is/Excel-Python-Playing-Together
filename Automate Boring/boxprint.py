#boxprint

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('The "symbol" length cannot be greater than 1')
    
    print(symbol * width)

    for i in range (height-2):
        print(symbol + (' ' * (width-2)) + symbol)

    print(symbol * width)
boxPrint('*', 15, 5)
boxPrint('0', 5, 16)