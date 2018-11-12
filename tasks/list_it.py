'''
create fucntion that list folowing names:
Daniel, Alicja,Tomek, Puala, Oktawia, Igor.
Fist place name in list and by loop print it like that:
1. Daniel
2. Alicja
... and like that
'''

def print_names():
    names = ['Daniel', 'Alicja', 'Tomek', 'Puala', 'Oktawia', 'Igor']
    num = 1

    for name in names:
        print(str(num) + '. ' + name)
        num += 1

print_names()
