sum = int (input())
n = int(input())
receipt = 0
for i in range (n): 
    a , b = map(int, input().split())
    price = a * b
    receipt += price
if sum == receipt:
    print("Yes")
else:
    print("No")
