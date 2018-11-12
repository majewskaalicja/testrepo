'''
create 2 functions that print soemthing like that

*************** <- this is function 1 where parameter is symbol, and number of symbols
Hello Daniel    <- fucntion that has name as parameter
*************** <- this is function 1

function that print this should have triggered functions inside and be called 'greeting'

'''
'''
def greeting(num, symbol):
    for x in range(1, num + 1):
        print(symbol * x)

greeting(1, '*')
print 
'''

def stars(symbol, numer):
    x = symbol
    x *= numer
    print(x)


def hello(name):
    print('Hello ' + name + '!Nice to meet you')

    
def greeting(name):
    stars('*', 10)
    hello(name)
    stars('*', 10)





