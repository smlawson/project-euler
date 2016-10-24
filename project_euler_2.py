i = 0 #primary index
m = 1 #first secondary index
n = 2 #second secondary index
s = 2 #sum of even-valued terms of the Fibonacci sequence whose values do not exceed four million 

while i <= 4000000: #considering only terms that do not exceed four million
    i = m + n #next term of the Fibonacci sequence
    if i%2 == 0: #test to see if i is even
        s = s + i #only add to sum if i is indeed even
    m = i #moving up one 'rung' of the Fibonacci sequence
    i = m + n #next term of the Fibonacci sequence
    if i%2 == 0: #test to see if i is even
        s = s + i #only add to sum if i is indeed even
    n = i #moving up one 'rung' of the Fibonacci sequence

print(s) #display final sum (this is the 'answer')
