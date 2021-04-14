N = int(input())
first = N // 1000
second = (N // 100) % 10
third = (N // 10) % 10
forth = N % 10
if str(first) + str(second) == str(forth) + str(third):
    print(1)
else:
    print(0)
