A = int(input())
B = int(input())
N = int(input())
costOfOne = A * 100 + B
totalCost = costOfOne * N
rub = totalCost // 100
kop = totalCost % 100
print(rub, kop)
