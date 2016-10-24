i = 1 #primary index
s = 0 #sum of all multiples of 3 or 5 below 1000

while i < 1000: #only considering natural numbers below 1000
    if i%3 == 0 or i%5 ==0: #test to see if i is a multiple of 3 or 5
        s = s + i #only multiples of 3 or 5 are considered in total sum
    i = i + 1 #raise i by 1 and test again

print(s) #display final sum (this is the 'answer')
