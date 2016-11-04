i = 2 # primary index (starting with the first prime number)
primes = [] # list of all prime numbers so far (initially empty)

import math # required for square root function
def is_prime(n): # prime-checking function (adapted from http://stackoverflow.com/questions/18833759/python-prime-number-checker)
    if n % 2 == 0 and n > 2: #any even number greater than 2 is not prime
        return False
    for x in range(3, int(math.sqrt(n)) + 1, 2): # tests all odd factors (greater than 1) up to the square root of the number in question
        if n % x == 0: # if i is a factor, n can't be prime
            return False
    return True # all numbers that pass this criteria should be prime


while len(primes) < 10002: # while the list of primes does not yet contain the 10001st prime number . . .
    if is_prime(i): # test the primary index
        primes.extend([i]) # if it's prime, add it to the list of primes
    i += 1 # raise the primary index by 1

print (primes[10000]) # once the list contains 10001 primes, display the 10001st one (the 'answer')
