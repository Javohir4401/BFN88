from os import system
system("cls")

dct = {'a' : 1, 'b' : 2, 'c' : 3}

main = {v: k for k, v in dct.items()}

print(main)