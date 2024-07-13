from os import system
system("cls")

def main (dct):
    
    Maxkeys = max(dct.keys())

    print("Maksimal keys:", Maxkeys)

dct = {'a': 5, 'b': 10, 'c': 3, 'd': 8}

main (dct)