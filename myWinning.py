'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
from random import shuffle
from itertools import combinations

lottery = list(range(1,49))
number = []
#print(lottery)

for i in range(5):
    shuffle(lottery)
    x = lottery.pop()
    number.append(x)


number.sort()
print(number)

def usingCombination():
    f = open('combinations.txt', 'a')
    for comb in combinations(range(1,50), 6):
        f.write(str(comb))
        f.write('\n')
    f.close()
