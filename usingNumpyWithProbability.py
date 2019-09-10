'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

import numpy as np
import itertools
import json


#print ('Hello World')


numberList = [val for val in range(1,51)]
#print(numberList)

probability = [1/len(numberList)] * len(numberList)
fileName = 'result.json'
result = itertools.combinations(numberList,5)
#with open(fileName,'w') as fn:
    #json.dump(str(list(result)),fn)
#print(list(result))

#print(probability)
#print(len(probability))
np.random.shuffle(numberList)
test = np.random.choice(numberList, 5, replace=False, p=probability)
test.sort()
print(test)



