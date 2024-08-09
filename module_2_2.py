first = int(input())
second = int(input())
third = int(input())
if first == second and second == third:
    up = 3
else:
    if first == second or first == third or second == third:
        up = 2
    else:
        up = 0
print(up)
