from os import system
system("cls")
from collections import Counter

def main (lst):

    sum = Counter(lst)

    num = sum.most_common(1)[0]

    return num

lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

natija = main(lst)

print(natija) # N soni M marta qatnashg