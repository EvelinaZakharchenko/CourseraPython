N = int(input())
hours = (N // 3600) % 24
minutes1 = (((N % 3600) // 60) // 10) % 10
minutes2 = ((N % 3600) // 60) % 10
secs1 = (((N % 3600) % 60) // 10) % 10
secs2 = ((N % 3600) % 60) % 10
print(hours, ":", minutes1, minutes2, ":", secs1, secs2, sep="")
