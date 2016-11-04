import math # required for square root function

# natural numbers m, n, and c must each be less than 1000 if they are to sum to 1000
for m in range (1,1000): 
    for n in range (1,1000):
        if m + n + math.sqrt((m*m) + (n*n)) == 1000: # if a + b + c = 1000 
            a = m
            b = n
            c = math.sqrt((m*m) + (n*n))
            break # once the unique triplet (a,b,c) is found, we are done

print(a) # (optional)
print(b) # (optional)
print(c) # (optional)
print(a*b*c) # displays the product of the Pythagorean triplet (the 'answer')
