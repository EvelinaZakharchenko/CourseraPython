N = int(input())
firstDigit = (N // 10) // 10
secondDigit = (N // 10) % 10
thirdDigit = N % 10
print(firstDigit+secondDigit+thirdDigit)
