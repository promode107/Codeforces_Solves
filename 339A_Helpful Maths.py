x = input().split('+')
x.sort()
ans = ""
for i in range(len(x)):
    ans += x[i]
    if i != len(x)-1:
        ans += '+'
print(ans)