def get_factorial(index):
    factorial = 1
    for i in range(1, index+1):
        factorial *= i
    return factorial


def digit_sum(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum

fac_100 = get_factorial(100)
print(digit_sum(fac_100))