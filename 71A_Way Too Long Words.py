n = int(input())
for i in range(n):
    w = input()
    l = len(w)
    if l > 10:
        print(w[0] + str(l-2) + w[l-1])
    else:
        print(w)