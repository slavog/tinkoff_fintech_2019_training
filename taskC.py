N, K = map(int, input().split())
length = [int(i) for i in input().split()]
optimal = sum(length)/(K+1)
parts = 2
available_cuts = K
while available_cuts != 0:
    log = max(length)
    cut_log = log
    if cut_log <= optimal:
        break
    while cut_log > optimal and available_cuts != 0:
        cut_log = log / parts
        if cut_log > optimal:
            parts += 1
        else:
            available_cuts -= parts-1
            length.remove(log)
            for i in range(parts):
                length.append(cut_log)
            parts = 2

if int(max(length)) == max(length):
    print(int(max(length)))
else:
    print(int(max(length))+1)
