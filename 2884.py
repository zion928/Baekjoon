hour, min = map(int, input().split())
if 0 <= hour <= 23 and 0 <= min <= 59:
    if min < 45:
        if hour > 0:
            hour = hour - 1
            min = min + 15
        else:
            hour = 23 + hour
            min = min + 15
    else:
        min = min - 45 

print(f"{hour} {min}") 