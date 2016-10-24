m = 1
n = 2
s = 2
i = 0

while i <= 4000000:
    i = m + n
    if i%2 == 0:
        s = s + i
    m = i
    i = m + n
    if i%2 == 0:
        s = s + i
    n = i

print(s)
