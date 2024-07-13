from os import system
system("cls")

def main(dct, key):
    if key in dct:
        del dct[key]
    return dct

dct = {'a': 1, 'b': 2, 'c': 3}

key = 'c'

natija = main(dct, key)

print(natija)