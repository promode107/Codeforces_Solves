n, k = map(int, input().split())
x = list(map(int, input().split()))

count = 0

for i in range(n):
    if x[i] >= x[k-1] and x[i] > 0:
        count += 1

print(count)