hour1 = int(input())
min1 = int(input())
sec1 = int(input())
hour2 = int(input())
min2 = int(input())
sec2 = int(input())
firstTime = hour1 * 3600 + min1 * 60 + sec1
secondTime = hour2 * 3600 + min2 * 60 + sec2
print(secondTime - firstTime)
