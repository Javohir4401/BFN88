from os import system
system("cls")
def main (dct):
    
    Maxvalue = max(dct.values())

    print("Maksimal value:", Maxvalue)

dct = {'a': 5, 'b': 10, 'c': 3, 'd': 8}

main (dct)