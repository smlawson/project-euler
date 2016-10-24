n = 600851475143
i = 3
l = 0
x = 0

import math

def is_prime(x):
    if x % 2 == 0:
        return False
    for y in range(3,int(math.sqrt(x)),2):
        if x % y == 0:
            return False
    return True

for i in range (3,int(math.sqrt(x)),2):
    if n%i == 0:
        if is_prime(i):
            l = i

print(l)
