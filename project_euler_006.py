s = 0 #sum of squares of all natural numbers 1,2,3,...,100
t = 0 #sum of all natural numbers 1,2,3,...,100

for i in range (1,101): #incrementally ascending through the first 100 natural numbers
    s = s + (i*i) #s grows by the the square of the ith natural number
    t = t + i #t grows by the ith natural number

print(s) #display s (optional)
print(t) # display t (optional)
print((t*t) - s) #display the difference between the square of the sum and the sum of the squares (this is the 'answer')
