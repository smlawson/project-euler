# Given number:
n = '73167176531330624919225119674426574742355349194934'\
    '96983520312774506326239578318016984801869478851843'\
    '85861560789112949495459501737958331952853208805511'\
    '12540698747158523863050715693290963295227443043557'\
    '66896648950445244523161731856403098711121722383113'\
    '62229893423380308135336276614282806444486645238749'\
    '30358907296290491560440772390713810515859307960866'\
    '70172427121883998797908792274921901699720888093776'\
    '65727333001053367881220235421809751254540594752243'\
    '52584907711670556013604839586446706324415722155397'\
    '53697817977846174064955149290862569321978468622482'\
    '83972241375657056057490261407972968652414535100474'\
    '82166370484403199890008895243450658541227588666881'\
    '16427171479924442928230863465674813919123162824586'\
    '17866458359124566529476545682848912883142607690042'\
    '24219022671055626321111109370544217506941658960408'\
    '07198403850962455444362981230987879927244284909188'\
    '84580156166097919133875499200524063689912560717606'\
    '05886116467109405077541002256983155200055935729725'\
    '71636269561882670428252483600823257530420752963450'

s = str(n) # Converts n into one string

# 13 digits in a row are each assigned a unique identifier (a-m)
a = 0 
b = 1
c = 2
d = 3
e = 4
f = 5
g = 6
h = 7
i = 8
j = 9
k = 10
l = 11
m = 12

# p denotes the greatest product of the 13 specified digits so far
p = (int(s[a]))*(int(s[b]))*(int(s[c]))*(int(s[d]))*(int(s[e]))*(int(s[f]))*(int(s[g]))*(int(s[h]))*(int(s[i]))*(int(s[j]))*(int(s[k]))*(int(s[l]))*(int(s[m]))

# The 13-digit 'substring' repeatedly shifts by 1 digit all the way through n, until m denotes the last digit of n  
while m < 999:
    a += 1
    b += 1
    c += 1
    d += 1
    e += 1
    f += 1
    g += 1
    h += 1
    i += 1
    j += 1
    k += 1
    l += 1
    m += 1

    #q denotes the product of the 13 specified digits during a given iteration
    q = (int(s[a]))*(int(s[b]))*(int(s[c]))*(int(s[d]))*(int(s[e]))*(int(s[f]))*(int(s[g]))*(int(s[h]))*(int(s[i]))*(int(s[j]))*(int(s[k]))*(int(s[l]))*(int(s[m]))

    #if q exceeds the current record for the largest product (p), p takes on the new value of q
    if q > p:
        p = q

print(p) #The final, greatest product of any 13-digit substring is displayed; this is the 'answer'
