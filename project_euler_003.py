n = 600851475143 #given number
i = 3 #primary index
l = 0 #largest prime factor of n
x = 1 #index for prime-checking fuction

import math #required for square root function

def is_prime(x): #prime-checking fuction with input 'x'
    if x % 2 == 0: #immediately fail test if x is even
        return False #even values of x cannot be prime
    for y in range(3,int(math.sqrt(x)),2): #testing values (3,5,7,...,sqrt(x)); multiples of 2 have already been thrown out
        if x % y == 0: #if x is divisible by any of these values, x cannot be prime
            return False #values of x divisble by anything other than 1 (or x) are not prime
    return True #every x that passes these criteria is prime

for i in range (3,int(math.sqrt(n)),2): #testing odd values between 3 and sqrt(n)
    if n%i == 0: #looking for factors of n
        if is_prime(i): #looking specifically for prime factors of n
            l = i #l takes on the value of the largest prime factor of n thus far

print(l) #display the largest prime factor of n (this is the 'answer')
