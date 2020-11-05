limit = 4000000
sum = 0
f = 1
s = 1
t = f + s
while t < limit:
    sum += t
    f = s + t
    s = t + f
    t = f + s

print(sum)