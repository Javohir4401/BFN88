from os import system
system("cls")

dct = {'a': 3,'b': 1,'c': 2}

natija = sorted(dct.items(), key=lambda i:i[1])

print(natija)