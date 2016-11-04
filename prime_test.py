import math # required for square root function
def is_prime(n): # prime-checking function (adapted from http://stackoverflow.com/questions/18833759/python-prime-number-checker)
    if n % 2 == 0 and n > 2: #any even number greater than 2 is not prime
        return False
    for x in range(3, int(math.sqrt(n)) + 1, 2): # tests all odd factors (greater than 1) up to the square root of the number in question
        if n % x == 0: # if i is a factor, n can't be prime
            return False
    return True # all numbers that pass this criteria should be prime
