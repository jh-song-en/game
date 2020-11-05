num = 999

def sum_by_div(div):
    tot = num // div
    return div * tot * (tot+1) // 2

answer = sum_by_div(3) + sum_by_div(5) - sum_by_div(15)

print(answer)