n = int(input())
if n % 2 == 0:
    n1 = n
else:
    n1 = n + 1
counter = 0
while n1 != 1 and n1 != 0:
    if n1 % 2 == 0:
        n1 = n1 // 2
        counter += 1
    else:
        n1 += 1
if n == 1:
    print(0)
else:
    print(counter)
