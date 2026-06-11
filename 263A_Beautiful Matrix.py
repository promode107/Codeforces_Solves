arr = []
for i in range(5):
    arr.append(list(map(int, input().split())))

m = 0
n = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            m, n = i, j
            break

count = 0
while m != 2 or n != 2:
    if m < 2:
        m += 1
        count += 1
    elif m > 2:
        m -= 1
        count += 1
    elif n < 2:
        n += 1
        count += 1
    elif n > 2:
        n -= 1
        count += 1

print(count)