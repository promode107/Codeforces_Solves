n = input()

count = 0
for ch in n:
    if ch == '4' or ch == '7':
        count += 1

if count > 0:
    lucky = True
    for ch in str(count):
        if ch != '4' and ch != '7':
            lucky = False
            break

    if lucky:
        print("YES")
    else:
        print("NO")
else:
    print("NO")