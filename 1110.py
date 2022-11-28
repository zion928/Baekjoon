n = int(input())
tmp = n
count = 0
x = -1
y = -1

while True:
    if tmp < 10:
        tmp = 11*tmp
        count += 1
        if tmp == n:
            break
    if tmp >= 10:
        x = int(tmp/10) 
        y = tmp % 10
        tmp = 10*y + int((x+y)%10)
        count += 1
        if tmp == n:
            break


print(f"{count}")
