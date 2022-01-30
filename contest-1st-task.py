a, b, c, d = map(int, input().split())
if d <= b:
    print(a)
else:
    print(a+(d-b)*c)
