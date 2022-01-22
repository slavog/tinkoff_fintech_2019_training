T = int(input())
for t in range(T):
    text = list(input())
    text.sort()
    if text[0] == text[1] and text[2] == text[3] and text[1] != text[2]:
        print('Yes')
    else:
        print('No')
