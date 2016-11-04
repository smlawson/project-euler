import math # required for square root function
def is_prime(n): # prime-checking function (adapted from http://stackoverflow.com/questions/18833759/python-prime-number-checker)
    if n % 2 == 0 and n > 2: #any even number greater than 2 is not prime
        return False
    for x in range(3, int(math.sqrt(n)) + 1, 2): # tests all odd factors (greater than 1) up to the square root of the number in question
        if n % x == 0: # if i is a factor, n can't be prime
            return False
    return True # all numbers that pass this criteria should be prime

s = 2 # the sum of all primes so far, starting with 2 (the first prime)

for x in xrange (3, 2000000, 2): # testing all odd numbers between 3 and 2,000,000
    if is_prime(x): # if a number is prime . . .
        s = s + x # . . . it gets added to the running total

print (s) # displays the final sum of all the primes below 2,000,000 (the 'answer')
