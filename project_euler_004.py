l = 0 #index that keeps track of the largest palindromic number so far
m = 100 #working index 1
n = 100 #working index 2

def test(m,n): #function that determines whether or now the product of its two inputs is a palindromic number
    s = str(m*n) #considers the product of the inputs as a string
    if m*n < 100000: #case for six-digit products
        if s[0] == s[4] and s[1] == s[3]: #palindrome test
            return True #'True' if product is a palindromic number
        else:
            return False #'False' if product is not a palindromic number
    else: #case for seven-digit products
        if s[0] == s[5] and s[1] == s[4] and s[2] == s[3]: #palindrome test
            return True #'True' if product is a palindromic number
        else:
            return False #'False' if product is not a palindromic number

for m in range (100, 999): #testing all three-digit numbers (first factor)
    for n in range (100, 999): #testing all three-digit numbers (second factor)
        if test(m,n): #if the product of the two factors is palindromic . . .
            if m*n > l: # . . . and if it exceeds the previous palindromic product . . .
                l = m*n # . . . this new product is registered as the largest palindromic product (so far)

print(l) #displays final (largest) palindromic product (this is the 'answer')
