hour, min = map(int, input().split())

add = int(input())
if 0 <= hour <= 23 and 0 <= min <= 59:
    if min + add >= 60:
        hour = int(hour + (min+add)/60) %24
        min = (min + add) % 60
    else:
        min = min+add 
print(f"{hour} {min}") 