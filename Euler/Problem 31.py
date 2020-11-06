

sum = 0

for a in range(0, 201, 1):
    print(a)
    for b in range(0, 201 - a, 2):
        for c in range(0, 201 - a - b, 5):
            for d in range(0, 201 - a - b - c, 10):
                for e in range(0, 201 - a - b - c- d, 20):
                    for f in range(0, 201- a - b - c- d - e, 50):
                        for g in range(0, 201- a - b - c- d - e-f, 100):
                            find = a+ b+ c+ d + e + f + g
                            if find == 200:
                                sum +=1
sum += 1
print(sum)

coins = [200, 100, 50, 20, 10, 5, 2, 1]
